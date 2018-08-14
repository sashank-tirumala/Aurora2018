#!/usr/bin/env python
import rospy
from std_msgs.msg import String
def talker():
    while not rospy.is_shutdown():
        rospy.init_node("test logger")
        rospy.logerr("hey there!!")
if(__name__ == "__main__"):
    talker()