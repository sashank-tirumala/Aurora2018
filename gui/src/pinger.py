#!/usr/bin/env python
import rospy
import CustomROSPing
from std_msgs.msg import String
def rosPinger():
    pub = rospy.Publisher("rosData",String,queue_size=10)   
    rospy.init_node("rosPinger",anonymous=False)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        str_data = ""
        data = CustomROSPing.rosnode_ping_all(True)
        for x in data:
            str_data=str_data+str(x)+"\n"
        pub.publish(str_data)
        rate.sleep()
if(__name__ == "__main__"):
    rosPinger()
