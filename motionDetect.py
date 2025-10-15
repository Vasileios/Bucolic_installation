from gpiozero import MotionSensor
from signal import pause
import time
from pythonosc.udp_client import SimpleUDPClient
import threading


osc_client = SimpleUDPClient("127.0.0.1", 57120)

pir = MotionSensor(18)

def motion_function():
    print("Motion Detected")
    osc_client.send_message("/motion", 1)
    time.sleep(10)

def no_motion_function():
    print("Motion stopped")
    osc_client.send_message("/motion", 0)
    time.sleep(10)

def heartbeat():
    while True:
        osc_client.send_message("/status", "alive")
        time.sleep(5)

heartbeat_thread = threading.Thread(target=heartbeat, daemon=True)
heartbeat_thread.start()

pir.when_motion = motion_function
time.sleep(10)
pir.when_no_motion = no_motion_function

time.sleep(10)

pause()
