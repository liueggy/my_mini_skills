# 常见错误与排障（Noetic）

## 1. 没有 source 环境
症状：`roscore: command not found`、找不到包。
处理：
- `source /opt/ros/noetic/setup.bash`
- `source ~/catkin_ws/devel/setup.bash`
- 写入 bashrc：`echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc`

## 2. 包未被 catkin 发现
症状：`[rospack] Error: package ... not found`。
处理：
- 包必须位于 `~/catkin_ws/src/<pkg>`
- `catkin_make` 后重新 `source devel/setup.bash`
- 检查 `package.xml` 与 `CMakeLists.txt`

## 3. 运行权限
症状：`Permission denied` 运行脚本失败。
处理：`chmod +x scripts/*.py` 或指定 `catkin_install_python`。

## 4. 话题名称不匹配 / 命名空间
症状：订阅不到数据。
处理：
- `rostopic list` 与 `rostopic info` 核对实际话题名
- 注意前导 `/` 绝对话题与相对话题
- 使用 `rqt_graph` 可视化

## 5. TF 断裂
症状：RViz 显示 `No transform from X to Y`。
处理：
- 用 `rosrun tf view_frames` 查看链路
- 确保广播者与监听者坐标系名一致
- 检查时间戳，仿真时启用 `use_sim_time`

## 6. 依赖缺失
症状：编译报找不到头文件/包。
处理：
- `rosdep install --from-paths src --ignore-src -r -y`
- 在 `package.xml` 添加 `build_depend` / `exec_depend`

## 7. Python 版本/Shebang
症状：运行脚本报 `python: not found` 或版本不一致。
处理：
- 使用 `#!/usr/bin/env python3`
- Noetic 默认 Python3

## 8. ROS_MASTER_URI/网络
症状：多机通信失败。
处理：
- 设置 `ROS_MASTER_URI` 与 `ROS_IP`/`ROS_HOSTNAME`
- 单机先不改网络变量，确认本地可通

## 9. bag 时间
症状：回放数据与节点时间不同步。
处理：
- `rosparam set use_sim_time true`
- `rosbag play --clock data.bag`

## 10. Launch 参数覆盖
症状：节点未读到期望参数。
处理：
- 检查 `<rosparam file=... command=load/>`
- 使用 `rosparam get` 验证最终参数
