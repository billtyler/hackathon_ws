#include "ros/ros.h"
#include "std_msgs/String.h"
#include "geometry_msgs/Twist.h"
#include <sstream>

void driveCallback(const geometry_msgs::TwistConstPtr &input)
{
    ROS_INFO("driving");
}

int main(int argc, char **argv)
{
    ros::init(argc, argv, "TB6612Driver");
    
    ros::NodeHandle n;
    
    ros::Subscriber sub = n.subscribe("cmd_vel", 1, driveCallback);

    ROS_INFO("starting");

    ros::spin();
    
    return 0;
}
