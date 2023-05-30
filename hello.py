#!/usr/bin/env python3

import rospy

rospy.init_node('my_node')

def main():
    rospy.loginfo("Working")

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
