#!/usr/bin/env python

import time
import picamera
import rospy
import numpy as np
import cv2

# Ros Messages
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

camera = picamera.PiCamera()

def publisher():
    pub = rospy.Publisher('CAUV_image', Image)
    rospy.init_node('CAUV_image_publisher')
    rate = rospy.Rate(1) # 10hz
    
    camera.resolution = (320, 240)
    camera.framerate = 24
    cv_image = np.empty((240, 320, 3), dtype=np.uint8)
    
    while not rospy.is_shutdown():
        
        rospy.loginfo("Capturing Image")
        
        camera.capture(cv_image, 'bgr')
        image_message = cv2_to_imgmsg(cv_image, encoding="passthrough")
        pub.publish(image_message)
        
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
