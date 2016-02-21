#! /usr/bin/python
from pixy import *
from ctypes import *
import rospy
from std_msgs.msg import String

# Pixy Python SWIG get blocks example #

# Initialize Pixy Interpreter thread #
pixy_init()

class Blocks (Structure):
    _fields_ = [ ("type", c_uint),
                 ("signature", c_uint),
                 ("x", c_uint),
                 ("y", c_uint),
                 ("width", c_uint),
                 ("height", c_uint),
                 ("angle", c_uint) ]

blocks = BlockArray(100)
frame = 0

# Publisher task #
def talker():
    print('test')
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        count = pixy_get_blocks(100, blocks)
        if count > 0:
            for index in range (0, count): 
	        proximity = blocks[index].width * blocks[index].height
	        ros_msg = '[sig=%d x=%d y=%d p=%3d a=%3d]' % (blocks[index].signature, blocks[index].x, blocks[index].y, proximity, blocks[index].angle)
                rospy.loginfo(ros_msg)
                pub.publish(ros_msg)
                rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
