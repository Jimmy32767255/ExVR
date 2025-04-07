from threading import Event
from utils.config import setup_config, save_config
from utils.data import setup_data, save_data
from utils.hotkeys import setup_hotkeys,apply_hotkeys
from utils.smoothing import setup_smoothing
from utils.hand_sender import setup_controller
from tracker.controller.controller import setup_gestures
import cv2

config=setup_config()
data,default_data = setup_data()
latest_data = [0.0] * (64 + 6 + 12 + 10 + 12 + 10 + 3+6)
stop_event = Event()
controller=setup_controller()
hotkey_config = setup_hotkeys()
smoothing_config = setup_smoothing()
gesture_config = setup_gestures()
face_landmarks=None
hand_landmarks=None
handedness=None
get_hand_video_track={"Left":False, "Right":False}

tongue_model=None
face_detector=None
hand_detector=None
start_time=cv2.getTickCount()
combo=[]
def has_combo(id):
    for i in combo:
        if i==id:
            return True
    return False

def update_configs():
    global config, data,default_data,latest_data,head_pos,controller,hotkey_config,smoothing_config,gesture_config
    config = setup_config()
    data,default_data=setup_data()
    latest_data = [0.0] * (64 + 6 + 12 + 10 + 12 + 10 + 3+6)
    controller=setup_controller()
    hotkey_config=setup_hotkeys()
    smoothing_config=setup_smoothing()
    gesture_config=setup_gestures()
    apply_hotkeys()

def save_configs():
    global config, data
    save_config(config)
    # save_data(data)
