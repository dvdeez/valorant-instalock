import sys
import ctypes
import pyautogui as gui
import time

def monitor_info():
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    width, height = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

    return width, height


def desired_agent(width, height, agent):
    match agent:
        case "astra":
            x_loc = width * 0.302083 # left-most agent in selection screen
            y_loc = height * 0.85185 # height of first row of agents
        case "breach":
            x_loc = (width * 0.302083) + (width * 0.04427) # one agent across from left-most
            y_loc = height * 0.85185
        case "brimstone":
            x_loc = (width * 0.302083) + 2(width * 0.04427) # two agents across from left-most
            y_loc = height * 0.85185
        case "chamber":
            x_loc = (width * 0.302083) + 3(width * 0.04427) # three agents across from left-most
            y_loc = height * 0.85185
        case "cypher":
            x_loc = (width * 0.302083) + 4(width * 0.04427) # four agents across from left-most
            y_loc = height * 0.85185
        case "fade":
            x_loc = (width * 0.302083) + 5(width * 0.04427) # five agents across from left-most
            y_loc = height * 0.85185
        case "harbor":
            x_loc = (width * 0.302083) + 6(width * 0.04427) # six agents across from left-most
            y_loc = height * 0.92593
        case "jett":
            x_loc = (width * 0.302083) + 7(width * 0.04427) # seven agents across from left-most
            y_loc = height * 0.85185
        case "kayo":
            x_loc = (width * 0.302083) + 8(width * 0.04427) # eight agents across from left-most
            y_loc = height * 0.85185
        case "killjoy":
            x_loc = (width * 0.302083) + 9(width * 0.04427) # nine agents across from left-most
            y_loc = height * 0.85185
        case "neon":
            x_loc = width * 0.302083 # left-most agent in selection screen
            y_loc = height * 0.92593 # height of second row of agents
        case "omen":
            x_loc = width * 0.302083 + (width * 0.04427) # one agent across from left-most
            y_loc = height * 0.92593 
        case "phoenix":
            x_loc = (width * 0.302083) + 2(width * 0.04427) # two agent across from left-most
            y_loc = height * 0.92593
        case "raze":
            x_loc = (width * 0.302083) + 3(width * 0.04427) # three agents across from left-most
            y_loc = height * 0.92593
        case "reyna":
            x_loc = (width * 0.302083) + 4(width * 0.04427) # four agents across from left-most
            y_loc = height * 0.92593
        case "sage":
            x_loc = (width * 0.302083) + 5(width * 0.04427) # five agents across from left-most
            y_loc = height * 0.92593
        case "skye":
            x_loc = (width * 0.302083) + 6(width * 0.04427) # six agents across from left-most
            y_loc = height * 0.92593
        case "sova":
            x_loc = (width * 0.302083) + 7(width * 0.04427) # seven agents across from left-most
            y_loc = height * 0.92593
        case "viper":
            x_loc = (width * 0.302083) + 8(width * 0.04427) # eight agents across from left-most
            y_loc = height * 0.92593
        case "yoru":
            x_loc = (width * 0.302083) + 9(width * 0.04427) # nine agents across from left-most
            y_loc = height * 0.92593
        case _:
            x_loc = "lig"
            y_loc = "ma"

    return x_loc, y_loc

def clicking(width, height, x_loc, y_loc):
    end_time = time.time() + 10
    while time.time() < end_time:
        gui.click(x_loc, y_loc)
        gui.click(width * 0.5, height * 0.75) # "lock in" button

def main():
    # retrieve monitor resolution
    width, height = monitor_info()
    # desired agent to play
    agent = sys.argv[1].lower()
    # retrieve agent coordinates
    x_loc, y_loc = desired_agent(width, height, agent)
    # give time to tab back into game
    print("YOU HAVE 5 SECONDS TO OPEN VALORANT")
    time.sleep(5)
    # begin instalock sequence
    clicking(width, height, x_loc, y_loc)

main()