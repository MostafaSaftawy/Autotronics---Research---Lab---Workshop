#! /usr/bin/env python3
from genpy import message
import rospy
from std_msgs.msg import String 

def CallBack_FN(msg):
    messagee = msg.data
    arr = messagee.split(',')
    rospy.loginfo("\n%s\n%s\n%s",arr[0],arr[1],arr[2])

def data_processing():
    rospy.init_node('data_processing')
    rospy.Subscriber('/raw_data', String, callback=CallBack_FN)
    rospy.spin()

if __name__ == "__main__":
    data_processing()