#! /usr/bin/env python3
import rospy
from std_msgs.msg import String, Int64

def CallBack_FN(msg):
    messagee = msg.data
    messagee = messagee.replace("Name: ","")
    messagee = messagee.replace(" Age: ","")
    messagee = messagee.replace(" Height: ","")
    string = messagee.split(',')
    print("Subscriber data: ")
    rospy.loginfo(msg)
    print("Publisher data: ")
    Name.publish(string[0])
    Age.publish(int(string[1]))
    Height.publish(int(string[2]))
    

def data_processing():
    rospy.init_node('data_processing')
    global Name ,Age ,Height 
    Name = rospy.Publisher('/Name', String, queue_size=10)
    Age = rospy.Publisher('/Age', Int64, queue_size=10)
    Height = rospy.Publisher('/Height', Int64, queue_size=10)
    rospy.Subscriber('/raw_data', String, callback=CallBack_FN)
    rospy.spin()

if __name__ == "__main__":
    data_processing()