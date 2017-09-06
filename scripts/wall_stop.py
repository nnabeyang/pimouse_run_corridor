#!/usr/bin/env python
import rospy, copy
#from geometry_msgs.msg import Twist
#from std_srvs.srv import Trigger, TriggerResponse
#from pimouse_ros.msg import LightSensorValues

#class WallStop():
#  def __init__(self):
#    self.cmd_vel = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

if __name__ == '__main__':
  rospy.init_node('wall_stop')

