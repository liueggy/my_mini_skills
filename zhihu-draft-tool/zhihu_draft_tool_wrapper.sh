#!/bin/sh
set -e

ENV_FILE="/var/minis/offloads/env_cookies_zhihu_com_1776499721.sh"
if [ ! -f "$ENV_FILE" ]; then
  echo "Cookie env file not found: $ENV_FILE" >&2
  exit 1
fi

. "$ENV_FILE"
COOKIE_STR="Hm_lvt_bff3d83079cef1ed8fc5e3f4579ec3b3=$COOKIE_HM_LVT_BFF3D83079CEF1ED8FC5E3F4579EC3B3; BEC=$COOKIE_BEC; SESSIONID=$COOKIE_SESSIONID; JOID=$COOKIE_JOID; osd=$COOKIE_OSD; _zap=$COOKIE__ZAP; d_c0=$COOKIE_D_C0; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=$COOKIE_HM_LVT_98BEEE57FD2EF70CCDD5CA52B9740C49; _ga=$COOKIE__GA; __zse_ck=$COOKIE___ZSE_CK; _xsrf=$COOKIE__XSRF; captcha_session_v2=$COOKIE_CAPTCHA_SESSION_V2; captcha_ticket_v2=$COOKIE_CAPTCHA_TICKET_V2; z_c0=$COOKIE_Z_C0; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=$COOKIE_HM_LPVT_98BEEE57FD2EF70CCDD5CA52B9740C49; HMACCOUNT=$COOKIE_HMACCOUNT"

python3 /var/minis/workspace/zhihu_draft_tool.py "$@" --cookie "$COOKIE_STR"
