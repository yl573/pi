#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String

def publisher():
    pub = rospy.Publisher('CAUV_test_message', String)
    rospy.init_node('CAUV_publisher')
    rate = rospy.Rate(2) # 10hz
    while not rospy.is_shutdown():
        myStr = "This is CAUV"
        rospy.loginfo(myStr)
        pub.publish(myStr)
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass