import ctypes
awareness = ctypes.c_int()
ctypes.windll.shcore.SetProcessDpiAwareness(2)

import yaml
import tkinter as tk
from const import *

# importing time and threading
import time
import threading
from pynput.mouse import Button, Controller

# pynput.keyboard is used to watch events of
# keyboard for start and stop of auto-clicker
from pynput.keyboard import Listener, KeyCode


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
                mouse.position = LOCK
                mouse.click(self.button)
                time.sleep(self.delay)
                mouse.position = self.agent_xy
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)


mouse = Controller()

window = tk.Tk()

window.title("Valorant Agent Picker")

window.geometry("200x440")

window.resizable(False, False)
agent_xy = ()


def get_cordinates(agent):
    return (
        START_X + (agent % COL) * SIZE + SIZE / 2,
        START_Y + (agent // COL) * SIZE + SIZE / 2,
    )

with open("agent.yaml", "r") as f:
    data = yaml.safe_load(f)
    
owned_agent = []

for key in data:
    if data[key] == True:
        owned_agent.append(key)


select = tk.StringVar(value="- Pick an agent -")
drop_down = tk.OptionMenu(window, select,"- Pick an agent -", *owned_agent)
drop_down.pack()


def pick():
    for i, agent in enumerate(owned_agent):
        if agent == select.get():
            x, y = get_cordinates(i)
            print(f"Agent {agent} is at ({x}, {y})")
            agent_xy = (x, y)
            click_thread = ClickMouse(DELAY, BUTTON, agent_xy)
            click_thread.start()

            def on_press(key):
                if key == START_STOP_HOTKEY:
                    if click_thread.running:
                        print("stop")
                        click_thread.stop_clicking()
                    else:
                        print("start")
                        click_thread.start_clicking()

                elif key == STOP_HOTKEY:
                    print("exit")
                    click_thread.exit()
                    listener.stop()

            with Listener(on_press=on_press) as listener:
                listener.join()
            return x, y




def dropdownupdate():
    drop_down["menu"].delete(0, "end")
    for agent in owned_agent:
        drop_down["menu"].add_command(label=agent, command=tk._setit(select, agent))


def handle_owned_agent():
    for key in state:
        if state[key].get() == True:
            if key not in owned_agent:
                owned_agent.append(key)
        if state[key].get() == False:
            if key in owned_agent:
                owned_agent.remove(key)

    owned_agent.sort()
    dropdownupdate()
    print(owned_agent)


state = {}

for key in data:
    state[key] = tk.BooleanVar()
    state[key].set(data[key])

button = tk.Button(window, text="Pick", command=pick).pack()

left_frame = tk.Frame(window, width=250)
left_frame.pack(side=tk.LEFT, fill=tk.Y)

right_frame = tk.Frame(window, width=250)
right_frame.pack(side=tk.RIGHT, fill=tk.Y)
def showcheckbox():
    astra = tk.Checkbutton(
        left_frame,
        text="Astra",
        variable=state["Astra"],
        onvalue=True,
        offvalue=False,
        command=handle_owned_agent,
    )
    astra.pack()

    breach = tk.Checkbutton(
        left_frame,
        text="Breach",
        variable=state["Breach"],
        onvalue=True,
        offvalue=False,
        command=handle_owned_agent,
    )
    breach.pack()

    brimstone = tk.Checkbutton(
        left_frame,
        text="Brimstone",
        variable=state["Brimstone"],
        onvalue=True,
        offvalue=False,
        command=handle_owned_agent,
    )
    brimstone.pack()

    cypher = tk.Checkbutton(
        left_frame,
        text="Cypher",
        variable=state["Cypher"],
        onvalue=True,
        offvalue=False,
        command=handle_owned_agent,
    )
    cypher.pack()

    chamber = tk.Checkbutton(
        left_frame,
        text="Chamber",
        variable=state["Chamber"],
        onvalue=True,
        offvalue=False,
        command=handle_owned_agent,
    )
    chamber.pack()

    deathlock = tk.Checkbutton(
        left_frame,
        text="Deathlock",
        variable=state["Deathlock"],
        onvalue=True,
        offvalue=False,
        command=handle_owned_agent,
    )
    deathlock.pack()

    fade = tk.Checkbutton(
        left_frame,
        text="Fade",
        variable=state["Fade"],
        onvalue=True,
        offvalue=False,
        command=handle_owned_agent,
    )
    fade.pack()

    gekko = tk.Checkbutton(
        left_frame,
        text="Gekko",
        variable=state["Gekko"],
        onvalue=True,
        offvalue=False,
        command=handle_owned_agent,
    )
    gekko.pack()

    habor = tk.Checkbutton(
        left_frame,
        text="Habor",
        variable=state["Habor"],
        onvalue=True,
        offvalue=False,
        command=handle_owned_agent,
    )
    habor.pack()

    jett = tk.Checkbutton(
        left_frame,
        text="Jett",
        variable=state["Jett"],
        onvalue=True,
        offvalue=False,
        command=handle_owned_agent,
    )
    jett.pack()

    kayo = tk.Checkbutton(
        left_frame,
        text="KAYO",
        variable=state["KAYO"],
        onvalue=True,
        offvalue=False,
        command=handle_owned_agent,
    )
    kayo.pack()

    killjoy = tk.Checkbutton(
        right_frame,
        text="Killjoy",
        variable=state["Killjoy"],
        onvalue=True,
        offvalue=False,
        command=handle_owned_agent,
    )
    killjoy.pack()

    neon = tk.Checkbutton(
        right_frame,
        text="Neon",
        variable=state["Neon"],
        onvalue=True,
        offvalue=False,
        command=handle_owned_agent,
    )
    neon.pack()

    omen = tk.Checkbutton(
        right_frame,
        text="Omen",
        variable=state["Omen"],
        onvalue=True,
        offvalue=False,
        command=handle_owned_agent,
    )
    omen.pack()

    phoenix = tk.Checkbutton(
        right_frame,
        text="Phoenix",
        variable=state["Phoenix"],
        onvalue=True,
        offvalue=False,
        command=handle_owned_agent,
    )
    phoenix.pack()

    raze = tk.Checkbutton(
        right_frame,
        text="Raze",
        variable=state["Raze"],
        onvalue=True,
        offvalue=False,
        command=handle_owned_agent,
    )
    raze.pack()

    reyna = tk.Checkbutton(
        right_frame,
        text="Reyna",
        variable=state["Reyna"],
        onvalue=True,
        offvalue=False,
        command=handle_owned_agent,
    )
    reyna.pack()

    sage = tk.Checkbutton(
        right_frame,
        text="Sage",
        variable=state["Sage"],
        onvalue=True,
        offvalue=False,
        command=handle_owned_agent,
    )
    sage.pack()

    skye = tk.Checkbutton(
        right_frame,
        text="Skye",
        variable=state["Skye"],
        onvalue=True,
        offvalue=False,
        command=handle_owned_agent,
    )
    skye.pack()

    sova = tk.Checkbutton(
        right_frame,
        text="Sova",
        variable=state["Sova"],
        onvalue=True,
        offvalue=False,
        command=handle_owned_agent,
    )
    sova.pack()

    viper = tk.Checkbutton(
        right_frame,
        text="Viper",
        variable=state["Viper"],
        onvalue=True,
        offvalue=False,
        command=handle_owned_agent,
    )
    viper.pack()

    yoru = tk.Checkbutton(
        right_frame,
        text="Yoru",
        variable=state["Yoru"],
        onvalue=True,
        offvalue=False,
        command=handle_owned_agent,
    )
    yoru.pack()

showcheckbox()

def onclose():
    # save data
    for key in state:
        if state[key].get():
            data[key] = True
        else:
            data[key] = False
    
    with open("agent.yaml", "w") as f:
        yaml.dump(data, f)
        
    window.destroy()

window.protocol("WM_DELETE_WINDOW", onclose)

window.mainloop()
