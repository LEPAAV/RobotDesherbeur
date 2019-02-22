#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
script de controle du robot:
commande proportionnelle par rapport à l'erreur sur l'angle et la distance
"""

# license removed for brevity
import rospy
from std_msgs.msg import String, Float64, Float64MultiArray, Empty
from math import atan2,pi




def commander_vitesse_roues(message, publishers):
    pub1, pub2, pub3 = publishers[0],publishers[1],publishers[2]
    r = message.data
    vitesse = 0.5*r + 0.3
    # print(r)
    if r > 0.167:
        pub1.publish(Float64(data = 2*vitesse))
        pub2.publish(Float64(data = 2*vitesse))
    else:
        pub3.publish(Empty())
        pub1.publish(Float64(data = 0))
        pub2.publish(Float64(data = 0))


def commander_angle_roues(message, publishers):
    pub1, pub2 = publishers[0],publishers[1]
    theta = -message.data/180*pi
    # theta = 0.2
    # print(theta)
    pub1.publish(Float64(data = theta))
    pub2.publish(Float64(data = theta))



if __name__ == '__main__':
    rospy.init_node('robotControl')
    pub_left_speed = rospy.Publisher('/desherbor_ensta/joint_left_bottom_wheel/command', Float64, queue_size = 1)
    pub_right_speed = rospy.Publisher('/desherbor_ensta/joint_right_bottom_wheel/command', Float64, queue_size = 1)
    pub_left_angle = rospy.Publisher('/desherbor_ensta/joint_left_top_wheel/command', Float64, queue_size = 1)
    pub_right_angle = rospy.Publisher('/desherbor_ensta/joint_right_top_wheel/command', Float64, queue_size = 1)
    pub_destroy = rospy.Publisher('/Destroy', Empty, queue_size = 1)
    rospy.Subscriber("/DISTANCE", Float64, commander_vitesse_roues, callback_args = [pub_left_speed,pub_right_speed,pub_destroy])
    rospy.Subscriber("/ORIENTATION", Float64, commander_angle_roues, callback_args = [pub_left_angle,pub_right_angle])
    rospy.spin()


    # while(1):
    #     roulement_roue_gauche()
    #     avancer()
    # try:
    # except rospy.ROSInterruptException:
    #     pass


