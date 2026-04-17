# Noetic 工作空间与最小示例

## 创建工作空间
```
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws
catkin_make
source ~/catkin_ws/devel/setup.bash
```
将 source 写入 bashrc：
```
echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc
```

## 创建最小 talker/listener（Python）
```
cd ~/catkin_ws/src
catkin_create_pkg demo_talk_listen rospy std_msgs
mkdir -p demo_talk_listen/scripts
```

scripts/talker.py：
```
#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def main():
    rospy.init_node('talker')
    pub = rospy.Publisher('/chatter', String, queue_size=10)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        pub.publish(String(data='hello world'))
        rate.sleep()

if __name__ == '__main__':
    main()
```

scripts/listener.py：
```
#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def cb(msg):
    rospy.loginfo('recv: %s', msg.data)

if __name__ == '__main__':
    rospy.init_node('listener')
    rospy.Subscriber('/chatter', String, cb)
    rospy.spin()
```

给可执行权限：
```
chmod +x demo_talk_listen/scripts/*.py
```

编辑 package.xml（添加 exec_depend）：
```
<exec_depend>rospy</exec_depend>
<exec_depend>std_msgs</exec_depend>
```

编辑 CMakeLists.txt（安装脚本）：
```
catkin_install_python(PROGRAMS
  scripts/talker.py
  scripts/listener.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
```

构建：
```
cd ~/catkin_ws && catkin_make
source devel/setup.bash
```

运行：
```
roscore
rosrun demo_talk_listen talker.py
rosrun demo_talk_listen listener.py
```

## Launch 与参数示例
创建 demo_talk_listen/launch/demo.launch：
```
<launch>
  <node pkg="demo_talk_listen" type="talker.py" name="talker" output="screen"/>
  <node pkg="demo_talk_listen" type="listener.py" name="listener" output="screen"/>
</launch>
```
运行：
```
roslaunch demo_talk_listen demo.launch
```
