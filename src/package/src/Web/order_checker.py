#! /usr/bin/python
from std_msgs.msg import String
import requests
import time
import rospy

def talker():
    get_url = 'http://ec2-54-86-127-71.compute-1.amazonaws.com:8000/api/order/'
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while True:
        result = requests.get(get_url).json()
        name = result.get('name')
        if name is not None:
            design = result.get('design_number')
            tag = result.get('tag_number')
            ros_msg  = 'name: %s, tag: %s' % (name, tag)
            rospy.loginfo(ros_msg)
            pub.publish(ros_msg)
        time.sleep(5)

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
