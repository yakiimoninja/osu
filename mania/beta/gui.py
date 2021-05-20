import tkinter as tk
from tkinter import Text
import cv2 as cv
import time
import key_actions
import window_cap
import win32gui


# OSU WINDOW SHOULD BE SET TO 1400 * 900 WINDOWED AND TOP LEFT CORNER FOR THIS TO WORK
# pos X 35, 85 140 200 250, 315, 365

def main():
        
    # For window tracking
    hwnd = win32gui.FindWindow(None, "osu!")
    window_pos = win32gui.GetWindowPlacement(hwnd)
    # Logic to isolate the X and Y
    window_pos = window_pos[4]
    window_start_x = window_pos[0]
    window_start_y = window_pos[1]

    loop_time = time.time()

    while True:
        screenshot = window_cap.window_cap_func(window_start_x, window_start_y)
        #color = screenshot[30, 85]
        #print(color[1])
        #cv.drawMarker(screenshot, (1683, 984), color = (255, 0, 255), markerType = cv.MARKER_CROSS, markerSize = 1, thickness = 1)
        cv.imshow('Computer Vision', screenshot)

        key_actions.play_mania('7', screenshot)

        print('FPS: {}'.format( 1 / (time.time() - loop_time)))
        loop_time = time.time()

        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            break

    print('Done')


root = tk.Tk()
root.geometry("250x100")

start_button = tk.Button(root, text = "Start", padx = 10, pady = 2, command = main)
start_button.configure(font=("Arial", 14))

stop_button = tk.Button(root, text = "Stop", padx = 10, pady = 2)
stop_button.configure(font=("Arial", 14))

clicked = tk.StringVar()
clicked.set("4 keys")
drop_list = tk.OptionMenu(root, clicked, "4 keys", "5 keys", "6 keys", "7 keys")
drop_list.configure(font=("Arial", 14))

drop_list.pack(side = tk.TOP, fill = tk.BOTH)
start_button.pack(side = tk.LEFT, fill = tk.BOTH, expand = tk.TRUE)
stop_button.pack(side = tk.RIGHT, fill = tk.BOTH, expand = tk.TRUE)


root.mainloop() 