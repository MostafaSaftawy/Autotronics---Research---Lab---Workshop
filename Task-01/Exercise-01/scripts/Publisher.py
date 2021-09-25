#! /usr/bin/env python3
import rospy
from std_msgs.msg import String

def  user_info_driver():
    rospy.init_node('user_info_driver')
    publisher = rospy.Publisher('/raw_data', String, queue_size=10)
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        my_msg = String()
        my_msg.data = "name: Rose, age: 20, height: 170"
        publisher.publish(my_msg)
        rate.sleep()
    

if __name__ == "__main__":
     user_info_driver()
    