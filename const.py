from pynput.mouse import Button, Controller
  
# pynput.keyboard is used to watch events of
# keyboard for start and stop of auto-clicker
from pynput.keyboard import Listener, KeyCode

COL = 11
ROW = 2

START_X = 500
START_Y = 880

SIZE = 80

LOCK = (960, 800)

DELAY = 0.05
BUTTON = Button.left
START_STOP_HOTKEY = KeyCode(char='p')
STOP_HOTKEY = KeyCode(char='o')
