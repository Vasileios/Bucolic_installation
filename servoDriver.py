"""Small example OSC server

This program listens to several addresses, and prints some information about
received packets.
"""
import argparse
import math
import time
#from gpiozero import MotionSensor
#from signal import pause

from adafruit_servokit import ServoKit

kit = ServoKit(channels=8)
from pythonosc.dispatcher import Dispatcher
from pythonosc import osc_server

#pir = MotionSensor(18)

def print_volume_handler(unused_addr, args, volume):
  print("[{0}] ~ {1}".format(args[0], volume))

def print_compute_handler(unused_addr, args, volume):
  try:
    print("[{0}] ~ {1}".format(args[0], args[1](volume)))
  except ValueError: pass

def main1(path: str, *osc_arguments):
    msg = osc_arguments[-1]
   # print("input message: {}".format(msg[1]))
    print(msg)
    msgOUT1 = int(msg) #+'whatever'
    #msgThr1 = int(msg)
    kit.servo[1].angle =msgOUT1
    #kit.continuous_servo[1].throttle = msgThr1
   # kit.servo[6].angle=msgOUT
def main2(path: str, *osc_arguments):
    msg = osc_arguments[-1]
    #print("input message: {}".format(msg[1]))
    print(msg)
    msgOUT3 = int(msg) #+'whatever'
    #msgThr3 = int(msg[1])
    #kit.servo[5].angle =msgOUT
    kit.servo[3].angle=msgOUT3
    #kit.continuous_servo[3].throttle = msgThr3

def main3(path: str, *osc_arguments):
    msg = osc_arguments[-1]
    print(msg)
    msgOUT5 = int(msg)
   # msgThr5 = int(msg[1])
    kit.servo[5].angle=msgOUT5
    #kit.continuous_servo[5].throttle = msgThr5

def main4(path: str, *osc_arguments):
    msg = osc_arguments[-1]
    print(msg)
    msgOUT6 = int(msg)
   # msgThr6 = int(msg[1])
    kit.servo[6].angle = msgOUT6
    #kit.continuous_servo[6].throttle = msgThr6

#def motion_function();
#    print("Motion Detected")

#def no_motion_function():
#    print("Motion stopped")

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip",
      default="127.0.0.1", help="The ip to listen on")
  parser.add_argument("--port",
      type=int, default=5005, help="The port to listen on")
  args = parser.parse_args()

  dispatcher = Dispatcher()
  #kit.servo[5].angle = 180
  out2 = dispatcher.map("/servo1", main1, "msgOUT1")
  out4 = dispatcher.map("/servo2", main2, "msgOUT3")
  out5 = dispatcher.map("/servo3", main3, "msgOUT5")
  out6 = dispatcher.map("/servo4", main4, "msgOUT6")
 # kit.servo[5].angle =msgOUT
#  dispatcher.map("/volume", print_volume_handler, "Volume")
#  dispatcher.map("/logvolume", print_compute_handler, "Log volume", math.log)

  server = osc_server.ThreadingOSCUDPServer(
      (args.ip, args.port), dispatcher)
  print("Serving on {}".format(server.server_address))
  server.serve_forever()
