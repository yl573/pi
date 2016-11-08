#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo("I heard something:  %s", data.data)
    
def listener():

    rospy.init_node('CAUV_subscriber')

    rospy.Subscriber("CAUV_test_message", String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()