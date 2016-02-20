#include "ros/ros.h"
#include "std_msgs/String.h"

#include <sstream>

void chatterCallback(const geometry_msgs::TwistConstPtr &input)
{
    ROS_INFO("driving");
}

int main(int argc, char **argv)
{
    ros::init(argc, argv, "TB6612 Driver");
    
    ros::NodeHandle n;
    
    cmd_vel_sub = node_.subscribe("cmd_vel", 1, &RoboClawNode::OnTwistCmd, this);
    ros::Subscriber sub = n.subscribe("chatter", 1000, chatterCallback);

    ros::spin();
    
    return 0;
}