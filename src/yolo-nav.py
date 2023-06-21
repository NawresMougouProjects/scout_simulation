#These are shebang and encoding declarations. They specify that the script should be run using the Python 3 interpreter and that the source code is encoded in UTF-8.
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#These lines import necessary modules and classes for working with ROS
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np
from geometry_msgs.msg import Twist

#This code defines a class named robot_camera. The __init__ method is the constructor that initializes the class
class robot_camera():
    def __init__(self):
        rospy.init_node("camera")
        rospy.Subscriber("/realsense_d435/color/image_raw", Image, self.camera_cb) #Subscribes to the topic /realsense_d435/color/image_raw to receive image messages and calls the camera_cb
        self.pub = rospy.Publisher("cmd_vel",Twist,queue_size = 10)
        self.vel = Twist() #Creates an instance variable vel of type Twist to store velocity commands.
        self.bridge = CvBridge() #Creates an instance variable bridge of type CvBridge to convert between ROS Image messages and OpenCV images.
        rospy.spin() #to keep the node running until it is explicitly shut down.

    def camera_cb(self, mesg):
        self.cap = self.bridge.imgmsg_to_cv2(mesg, "bgr8")

        #These lines perform image processing operations to detect red regions in the image. It first defines lower and upper threshold values for the red color in HSV color space
        lower_red = np.array([0,50,50]) #example value
        upper_red = np.array([10,255,255])
        
        hsv = cv2.cvtColor(self.cap, cv2.COLOR_BGR2HSV) #Then it converts the captured image self.cap from BGR to HSV color space using cv2.cvtColor.
    
        mask = cv2.inRange(hsv, lower_red, upper_red)
        mask = cv2.erode(mask, (5, 5), iterations=9)
        mask = cv2.medianBlur(mask, 7)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, (5, 5))
        mask = cv2.dilate(mask, (5, 5), iterations=1) #Next, it applies a series of image processing operations (erode, medianBlur, morphologyEx, dilate) to obtain a binary mask (mask) where red regions are highlighted. The threshold function is used to convert the mask to a binary image.

        _, thresh = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)
    
        cnts,_ = cv2.findContours(thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE)
        #it uses cv2.findContours to find contours in the binary image, which represent the red regions.
        frame_center_x = self.cap.shape[1]/2
        frame_center_y = self.cap.shape[0]/2
        #These lines calculate the center coordinates of the image (frame_center_x and frame_center_y) by dividing the width and height of self.cap by 2.
        if len(cnts) > 0:
            c = max(cnts, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)

            cv2.circle(self.cap, (int(x), int(y)),int(radius),(0, 0, 255), 2)
            cv2.putText(self.cap, "X : " + str(round(x,2)), (int(x)+int(radius)+5,int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
            cv2.putText(self.cap, "Y : " + str(round(y,2)), (int(x)+int(radius)+5,int(y)+35), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
            
            #Finds the contour with the maximum area using max and cv2.contourArea and assigns it to c.Calculates the minimum enclosing circle for the contour using cv2.minEnclosingCircle and retrieves the center coordinates (x, y) and radius.Draws the circle on self.cap using cv2.circle and adds a label for the x and y coordinates using cv2.putText

            hata_x = int(x) - int(frame_center_x)
            
            self.vel.linear.x = 0.07 # ileri gitmesi icin
            self.vel.angular.z = -hata_x/10000
            self.pub.publish(self.vel)
            if radius > 150: #If the radius of the red region exceeds a threshold (150), it stops the linear and angular velocities to halt the robot's movement.
                self.vel.linear.x = 0.0
                self.vel.angular.z = 0.0
                self.pub.publish(self.vel)

        else:
            self.vel.linear.x = 0.0
            self.vel.angular.z = 0.07
            self.pub.publish(self.vel) # If no contours are found, it assigns a constant angular velocity to rotate the robot until a red region is detected.

         #These lines calculate the error (hata_x) between the x-coordinate of the detected red region (x) and the center of the image (frame_merkez_x). It then assigns a linear velocity command to self.hiz_mesg.linear.x to move forward (0.07). The angular velocity command (self.hiz_mesg.angular.z) is calculated based on the error to align the robot with the red region.

        cv2.imshow("frame", self.cap)
        cv2.waitKey(1)
        #These lines display the image self.cap with the name "frame" using cv2.imshow and wait for a key press for 1 millisecond using cv2.waitKey(1).
  
nesne = robot_camera()
#Creates an instance of the robot_camera class, which initializes the necessary ROS node, subscribes to the image topic, and starts processing the received images.


