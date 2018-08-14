#/usr/bin/env python
import rospy
from geometry_msgs.msg import Vector3
def talker():
    pub = rospy.Publisher("feedback",Vector3,queue_size = 10)
    rospy.init_node("test",anonymous = True)
    rate = rospy.Rate(10)
    msg1 = Vector3()

    while not rospy.is_shutdown() : 
        msg1.x = 0.785
        msg1.y = 3.14
        msg1.z = 1.57
        pub.publish(msg1)
        rate.sleep()

if(__name__=="__main__"):
    talker()

        