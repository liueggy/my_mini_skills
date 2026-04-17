# ROS Noetic CLI 速查表

## 环境与工作空间
- 安装后加载环境：`source /opt/ros/noetic/setup.bash`
- 创建工作空间：`mkdir -p ~/catkin_ws/src && cd ~/catkin_ws && catkin_make`
- 加入 bashrc：`echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc`
- 查找包路径：`rospack find <pkg>`，`roscd <pkg>`

## 包与构建
- 创建包：`cd ~/catkin_ws/src && catkin_create_pkg <pkg> rospy roscpp std_msgs`
- 构建：`cd ~/catkin_ws && catkin_make`
- 清理：`cd ~/catkin_ws && catkin_make clean`
- 依赖安装：`rosdep install --from-paths src --ignore-src -r -y`

## 运行与管理
- 启动核心：`roscore`
- 运行节点：`rosrun <pkg> <node>`
- 启动 launch：`roslaunch <pkg> <file.launch>`
- 节点列表：`rosnode list`，详情：`rosnode info <node>`

## Topic
- 列表：`rostopic list`
- 监听：`rostopic echo <topic>`
- 频率：`rostopic hz <topic>`
- 类型：`rostopic type <topic>` -> `rosmsg show <type>`
- 发布（示例）：`rostopic pub /chatter std_msgs/String "data: 'hello'" -r 10`

## Service
- 列表：`rosservice list`
- 详情：`rosservice info <srv>`
- 类型：`rosservice type <srv>` -> `rossrv show <type>`
- 调用：`rosservice call /clear_costmaps {}` 或 `rosservice call /set_bool "data: true"`

## 参数
- 列表：`rosparam list`
- 读取：`rosparam get <name>`
- 设置：`rosparam set <name> <value>`
- 加载 YAML：`rosparam load config/params.yaml`

## TF / 可视化 / 录包
- 生成 TF 图：`rosrun tf view_frames && evince frames.pdf`
- TF 树可视化：`rosrun rqt_tf_tree rqt_tf_tree`
- 图形化关系：`rqt_graph`
- RViz：`rviz`，加载配置：`rviz -d rviz/default.rviz`
- 录制：`rosbag record -a`，回放：`rosbag play data.bag`，信息：`rosbag info data.bag`

## Gazebo
- 启动空世界：`roslaunch gazebo_ros empty_world.launch`
- 加载模型：`roslaunch <pkg> <gazebo.launch>`

## 常见路径
- 工作空间：`~/catkin_ws`
- 源码：`~/catkin_ws/src/<pkg>`
- 构建输出：`~/catkin_ws/devel`

## 诊断常用
- 检查环境：`echo $ROS_MASTER_URI`，`echo $ROS_PACKAGE_PATH`（注意：在文档中展示，不在对话中直接回显变量值）
- 检查订阅发布：`rqt_graph`
- bag 回放联调：`rosbag play --clock data.bag` + `use_sim_time: true`
