# importing time and threading
import time
import threading
from main import LOCK
from pynput.mouse import Button, Controller
  
# pynput.keyboard is used to watch events of
# keyboard for start and stop of auto-clicker
from pynput.keyboard import Listener, KeyCode

DELAY = 0.05
BUTTON = Button.left
START_STOP_HOTKEY = KeyCode(char='p')
STOP_HOTKEY = KeyCode(char='o')

class ClickMouse(threading.Thread):
    def __init__(self, delay, button, agent_xy):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.agent_xy = agent_xy
        self.running = False
        self.program_running = True
  
    def start_clicking(self):
        self.running = True
  
    def stop_clicking(self):
        self.running = False
  
    def exit(self):
        self.stop_clicking()
        self.program_running = False
  
    def run(self):
        while self.program_running:
            while self.running:
                mouse.move(LOCK)
                mouse.click(self.button)
                time.sleep(self.delay)
                mouse.move(self.agent_xy)
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)
            
mouse = Controller()
click_thread = ClickMouse(DELAY, BUTTON)
click_thread.start()

def on_press(key):
    if key == START_STOP_HOTKEY:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
            
    elif key == STOP_HOTKEY:
        click_thread.exit()
        listener.stop()
            
with Listener(on_press=on_press) as listener:
    listener.join()
