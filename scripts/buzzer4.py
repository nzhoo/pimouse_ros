#!/usr/bin/env python
#encoding: utf8
import rospy, actionlib
from pimouse_ros.msg import MusicAction, MusicResult, MusicFeedback

from std_msgs.msg import UInt16

def write_freq(hz=0):
    bfile = "/dev/rtbuzzer0"
    try:
        with open(bfile,"w") as f:
            f.write(str(hz) + "\n")
    except IOError:
        rospy.logerr("can't write to " + bfile)

def exec_music(goal): pass

def recv_buzzer(data):
    write_freq(data.data)

if __name__ == '__main__':
    rospy.init_node('buzzer')
    rospy.Subscriber("buzzer", UInt16, recv_buzzer)
    music = actionlib.SimpleActionServer('music', MusicAction, exec_music, False) # 追加
    music.start()                                                                 # 追加
    rospy.on_shutdown(write_freq)                                                 # 追加
    rospy.spin()
