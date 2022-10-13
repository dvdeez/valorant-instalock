import sys
import ctypes
import pyautogui as gui
import time

# user32 = ctypes.windll.user32
# user32.SetProcessDPIAware()
# screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)


def desired_agent(agent):
    match agent:
        case "astra":
            x_loc = 580
            y_loc = 920
        case "breach":
            x_loc = 665
            y_loc = 920
        case "brimstone":
            x_loc = 750
            y_loc = 920
        case "chamber":
            x_loc = 835
            y_loc = 920
        case "cypher":
            x_loc = 920
            y_loc = 920
        case "fade":
            x_loc = 1005
            y_loc = 920
        case "harbor":
            x_loc = 0
            y_loc = 0
        case "jett":
            x_loc = 1090
            y_loc = 920
        case "kayo":
            x_loc = 1175
            y_loc = 920
        case "killjoy":
            x_loc = 1260
            y_loc = 920
        case "neon":
            x_loc = 1345
            y_loc = 920
        case "omen":
            x_loc = 580
            y_loc = 1000
        case "phoenix":
            x_loc = 665
            y_loc = 1000
        case "raze":
            x_loc = 750
            y_loc = 1000
        case "reyna":
            x_loc = 835
            y_loc = 1000
        case "sage":
            x_loc = 920
            y_loc = 1000
        case "skye":
            x_loc = 1005
            y_loc = 1000
        case "sova":
            x_loc = 1090
            y_loc = 1000
        case "viper":
            x_loc = 1175
            y_loc = 1000
        case "yoru":
            x_loc = 1260
            y_loc = 1000
        case _:
            x_loc = "lig"
            y_loc = "ma"

    return x_loc, y_loc

def clicking(x_loc, y_loc):
    end_time = time.time() + 10
    while time.time() < end_time:
        gui.click(x_loc, y_loc)
        gui.click(960, 810) # "lock in" button

def main():
    agent = sys.argv[1].lower()
    start_time = time.time()
    
    # retrieve agent coordinates
    x_loc, y_loc = desired_agent(agent)
    # give time to tab back into game
    print("YOU HAVE 5 SECONDS TO OPEN VALORANT")
    time.sleep(5)
    # begin instalock sequence
    clicking(x_loc, y_loc)

main()