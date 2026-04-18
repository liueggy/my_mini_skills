#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Zhihu draft tool (prototype)

当前能力：
- create: 基于现有草稿接口创建新草稿
- get: 读取指定草稿
- update: 更新指定草稿

增强字段：
- title
- content
- summary
- comment_permission
- table_of_contents_enabled
- title_image

用法示例：
  python3 zhihu_draft_tool.py create --cookie 'xxx' --base-id 2028607956032176996 --title '标题' --content '正文'
  python3 zhihu_draft_tool.py create --cookie 'xxx' --base-id 2028607956032176996 --title '标题' --content-file /path/body.txt
  python3 zhihu_draft_tool.py get --cookie 'xxx' --id 2028860692585881962
  python3 zhihu_draft_tool.py update --cookie 'xxx' --id 2028860692585881962 --title '新标题' --summary '摘要'
"""

import argparse
import json
from urllib import request, error


def make_headers(cookie: str, method: str = "GET"):
    headers = {
        "Cookie": cookie,
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Safari/605.1.15",
        "Accept": "application/json, text/plain, */*",
        "Referer": "https://zhuanlan.zhihu.com/write",
        "Origin": "https://zhuanlan.zhihu.com",
    }
    if method in ("POST", "PATCH"):
        headers["Content-Type"] = "application/json"
    return headers


def http_json(url: str, cookie: str, method: str = "GET", payload=None):
    data = None
    if payload is not None:
        data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    req = request.Request(url, data=data, headers=make_headers(cookie, method), method=method)
    try:
        with request.urlopen(req, timeout=30) as resp:
            raw = resp.read().decode("utf-8", "ignore")
            return resp.status, raw
    except error.HTTPError as e:
        raw = e.read().decode("utf-8", "ignore")
        return e.code, raw


def read_text_arg(text_value=None, file_path=None):
    if file_path:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    return text_value


def get_draft(cookie: str, draft_id: str):
    url = f"https://zhuanlan.zhihu.com/api/articles/{draft_id}/draft"
    return http_json(url, cookie, "GET")


def apply_optional_fields(payload: dict, *, title=None, content=None, summary=None,
                          comment_permission=None, table_of_contents_enabled=None,
                          title_image=None):
    if title is not None:
        payload["title"] = title
    if content is not None:
        payload["content"] = content
        # 从实测看，summary 常会同步为正文简要文本；若未单独传 summary，可保留原值
        if summary is None:
            payload["summary"] = content
    if summary is not None:
        payload["summary"] = summary
    if comment_permission is not None:
        payload["comment_permission"] = comment_permission
    if table_of_contents_enabled is not None:
        payload.setdefault("settings", {})
        payload["settings"].setdefault("table_of_contents", {})
        payload["settings"]["table_of_contents"]["enabled"] = bool(table_of_contents_enabled)
    if title_image is not None:
        payload["title_image"] = title_image
    return payload


def create_draft(cookie: str, base_id: str, *, title: str, content: str,
                 summary=None, comment_permission=None,
                 table_of_contents_enabled=None, title_image=None):
    url = f"https://zhuanlan.zhihu.com/api/articles/{base_id}/draft"
    payload = {
        "title": title,
        "content": content,
    }
    payload = apply_optional_fields(
        payload,
        title=title,
        content=content,
        summary=summary,
        comment_permission=comment_permission,
        table_of_contents_enabled=table_of_contents_enabled,
        title_image=title_image,
    )
    return http_json(url, cookie, "POST", payload)


def update_draft(cookie: str, draft_id: str, *, title=None, content=None, summary=None,
                 comment_permission=None, table_of_contents_enabled=None,
                 title_image=None):
    status, raw = get_draft(cookie, draft_id)
    if status != 200:
        return status, raw
    current = json.loads(raw)
    payload = dict(current)
    payload = apply_optional_fields(
        payload,
        title=title,
        content=content,
        summary=summary,
        comment_permission=comment_permission,
        table_of_contents_enabled=table_of_contents_enabled,
        title_image=title_image,
    )
    url = f"https://zhuanlan.zhihu.com/api/articles/{draft_id}/draft"
    return http_json(url, cookie, "PATCH", payload)


def main():
    parser = argparse.ArgumentParser(description="Zhihu draft tool prototype")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_get = sub.add_parser("get")
    p_get.add_argument("--cookie", required=True)
    p_get.add_argument("--id", required=True)

    p_create = sub.add_parser("create")
    p_create.add_argument("--cookie", required=True)
    p_create.add_argument("--base-id", required=True)
    p_create.add_argument("--title", required=True)
    p_create.add_argument("--content")
    p_create.add_argument("--content-file")
    p_create.add_argument("--summary")
    p_create.add_argument("--comment-permission", choices=["all", "none", "registered_only"])
    p_create.add_argument("--table-of-contents-enabled", action="store_true")
    p_create.add_argument("--title-image")

    p_update = sub.add_parser("update")
    p_update.add_argument("--cookie", required=True)
    p_update.add_argument("--id", required=True)
    p_update.add_argument("--title")
    p_update.add_argument("--content")
    p_update.add_argument("--content-file")
    p_update.add_argument("--summary")
    p_update.add_argument("--comment-permission", choices=["all", "none", "registered_only"])
    p_update.add_argument("--table-of-contents-enabled", action="store_true")
    p_update.add_argument("--title-image")

    args = parser.parse_args()

    if args.cmd == "get":
        status, raw = get_draft(args.cookie, args.id)
    elif args.cmd == "create":
        content = read_text_arg(args.content, args.content_file)
        if content is None:
            parser.error("create requires --content or --content-file")
            return
        status, raw = create_draft(
            args.cookie,
            args.base_id,
            title=args.title,
            content=content,
            summary=args.summary,
            comment_permission=args.comment_permission,
            table_of_contents_enabled=args.table_of_contents_enabled,
            title_image=args.title_image,
        )
    elif args.cmd == "update":
        content = read_text_arg(args.content, args.content_file)
        status, raw = update_draft(
            args.cookie,
            args.id,
            title=args.title,
            content=content,
            summary=args.summary,
            comment_permission=args.comment_permission,
            table_of_contents_enabled=args.table_of_contents_enabled,
            title_image=args.title_image,
        )
    else:
        parser.error("unknown command")
        return

    print(json.dumps({"status": status, "data": json.loads(raw) if raw.strip().startswith(("{", "[")) else raw}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
