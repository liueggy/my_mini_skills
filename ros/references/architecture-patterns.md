# 常见架构模式（Noetic 导向）

## 1. 移动机器人导航（2D LiDAR）
- 传感器：`/scan` -> `slam_gmapping` 或 `hector_slam`
- 定位：`amcl`（基于地图）
- 地图服务器：`map_server`
- 规划：`move_base`（global + local planner）
- 控制输出：`/cmd_vel`
- TF：`map -> odom -> base_link -> laser`
- 可视化：`rviz`

## 2. 深度相机感知
- 传感器：`/camera/color/image_raw`、`/camera/depth/points`
- 同步：`message_filters`
- 算法：目标检测/分割 -> 发布 `MarkerArray`
- TF：`base_link -> camera_link`

## 3. 机械臂（MoveIt for ROS1）
- 驱动：`hardware_interface` + 控制器
- MoveIt：规划场景 + 运动规划
- 交互：`move_group`，发布路径到控制器
- TF：`base_link -> tool0`

## 4. 多机协作（ROS1）
- 统一 master：设置 `ROS_MASTER_URI`
- 区分命名空间：`namespace:=robot1/robot2`
- 同步时钟：`chrony` 或 `ntp`

## 5. 数据录制回放工作流
- 线上：按模块落盘关键 topic
- 线下：`rosbag play --pause` + `--clock` + 逐步调算法

## 6. Launch 组织建议
- `bringup/`：驱动与基础服务
- `mapping/`：建图
- `nav/`：导航
- `sim/`：仿真
- 在顶层 `bringup.launch` 里通过 `include` 组合

## 7. 配置与参数
- 将可调参数集中到 `config/*.yaml`
- Launch 中使用 `<rosparam file="config/xxx.yaml" command="load"/>`
- 节点内用 `ros::param` 或 `rospy.get_param` 读取

## 8. 包结构模板
```
<package>
  launch/
  config/
  scripts/ or src/
  urdf/ (可选)
  rviz/ (可选)
  CMakeLists.txt
  package.xml
</package>
```
