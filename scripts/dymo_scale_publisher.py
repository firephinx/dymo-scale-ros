from dymo import scale
import rospy
from std_msgs.msg import Int32

pub = rospy.Publisher('dymo_scale', Int32, queue_size=10)
rospy.init_node('dymo_scale_publisher')
r = rospy.Rate(10) # 10hz
usb=None

while not rospy.is_shutdown():
    if usb is None:
        try:
            usb = scale.USB()
        except:
            pass
    else:
        try:
            weight=usb.get_weight_grams()
            pub.publish(weight)
            r.sleep()
        except:
            usb = None
