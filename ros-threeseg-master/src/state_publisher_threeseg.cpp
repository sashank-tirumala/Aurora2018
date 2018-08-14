#include <string>
#include <ros/ros.h>
#include <sensor_msgs/JointState.h>
#include <tf/transform_broadcaster.h>
#include <geometry_msgs/Vector3.h>
#include <geometry_msgs/Twist.h>

double joint1= 0;
double joint2 =0;
double joint3 =0;
double joint4 =0;
double joint5 =0;
void armCallback(const geometry_msgs::Twist::ConstPtr& msg)
{
  joint1 = msg->linear.x;
  joint2 = msg->linear.y+1.57;
  joint3 = msg->linear.z;
  joint4 = msg->angular.x;
  joint5 = msg->angular.y;
  
}

int main(int argc, char** argv) {
  ros::init(argc, argv, "state_publisher_threeseg");
  ros::NodeHandle n;
  ros::Publisher joint_pub = n.advertise<sensor_msgs::JointState>("joint_states", 1);
  tf::TransformBroadcaster broadcaster;
  ros::Rate loop_rate(3);
   ros::Subscriber sub = n.subscribe("feedback",1000 , armCallback);
  // Robot state
  // Message declarations
  geometry_msgs::TransformStamped odom_trans;
  sensor_msgs::JointState joint_state;
  odom_trans.header.frame_id = "world";
  odom_trans.child_frame_id = "base";
  broadcaster.sendTransform(odom_trans);

  // Define joint state
  while(true)
  {
  joint_state.name.resize(5);
  joint_state.position.resize(5);
  joint_state.name[0] ="joint1";
  joint_state.name[1] ="joint2";
  joint_state.name[2] ="joint3";
  joint_state.name[3] ="joint4";
  joint_state.name[4] ="joint5";
  joint_state.header.stamp = ros::Time::now();
  joint_state.position[0] = joint1;
  joint_state.position[1] = joint2;
  joint_state.position[2] = joint3;
  joint_state.position[3] = joint4;
  joint_state.position[4] = joint5;
  // Send the joint state and transform
  joint_pub.publish(joint_state);
  ros::spinOnce();
  // This will adjust as needed per iteration
  loop_rate.sleep();
  }
  ros::spin();
  return 0;
}