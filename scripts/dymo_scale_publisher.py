from dymo import scale
import rospy
from std_msgs.msg import Int16

pub = rospy.Publisher('dymo_scale', Int16, queue_size=10)
rospy.init_node('dymo_scale_publisher')
r = rospy.Rate(10) # 10hz

while not rospy.is_shutdown():
   try:
      pub.publish(usb.get_weight_grams())
      r.sleep()
   except:
      try:
         usb = scale.USB()
