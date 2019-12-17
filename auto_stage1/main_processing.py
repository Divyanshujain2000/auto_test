#!/usr/bin/env python
import rospy
import nav_to_goal_1 as nav
from geometry_msg.msg import Point
from sensor_msgs.msg import NavSatFix
from sensor_msgs.msg import LaserScan

lat2 = 0.0
lon2 = 0.0
bearing = 0.0
distance = 0.0

def callback_gps(data):
    plat = data.latitude /rtd  #present latitude
    plon = data.longitude /rtd #present longitude
    count=count+1
def callback_imu(data_imu):
    yaw = data_imu.x
    pitch = data_imu.y
    roll = data_imu.z
    count=count+1
def listener():
    rospy.Subscriber("imu_node", Point , callback_imu)
    rospy.Subscriber("gps_node", NavSatFix , callback_gps)
    #rospy.Subscriber("lidar_node", LaserScan , callback_lidar)
    if(count==3):
        count=0
        nav.start_calc(yaw,plat,plon)

        

if __name__ == '__main__':
    listener()