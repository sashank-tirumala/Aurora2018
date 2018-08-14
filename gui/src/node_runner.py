#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher("node_runner",String, queue_size = 10)
    rospy.init_node("talker",anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        data = open("/home/sashank/aurora2018-master_new/src/gui/src/text_files/run_pinger.txt","r")
        if(data.readline() == '1'):
            pub.publish("1")
        rate.sleep()
        

if(__name__ == "__main__"):
    talker()
