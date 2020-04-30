import roslib; roslib.load_manifest('my_simulations')
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg

# Keyboard in Linux
import sys
import tty
import termios

def getKey():
    fd = sys.stdin.fileno()
    original_attributes = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, original_attributes)
    return ch

def arm():
    group = moveit_commander.MoveGroupCommander("arm")
    
    # We can get the joint values from the group and adjust some of the values:
    joint_goal = group.get_current_joint_values()
    joint_goal[0] = 0
    joint_goal[1] = -pi/4
    joint_goal[2] = 0
    joint_goal[3] = -pi/2

    # The go command can be called with joint values, poses, or without any
    # parameters if you have already set the pose or joint target for the group
    group.go(joint_goal, wait=True)

    # Calling ``stop()`` ensures that there is no residual movement
    group.stop()


if __name__='__main__':
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node('turtle3_arm',nonymous=True)
    try:
        arm()

    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")