#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback(msg):
	rospy.loginfo(rospy.get_caller_id() + "I heard %s", msg.data)

def main():
	rospy.init_node('test_subscriber')
	rospy.Subscriber("/test", String, callback)
	rospy.spin()#You need this line, but it works in some cases without
	
if __name__ == '__main__':
	main()
