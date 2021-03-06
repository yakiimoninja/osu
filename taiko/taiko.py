import cv2 as cv
import time
import key_actions
import window_cap
import win32api, win32con


# OSU WINDOW SHOULD BE SET TO 1400 * 900 WINDOWED
# key pos X 35, 85 140 200 250, 315, 365

img = cv.imread("playing.png")
time.sleep(3)
# For window position tracking
window_start_x = window_cap.window_tracking('x')
window_start_y = window_cap.window_tracking('y')

# Presses Enter key
win32api.keybd_event(13, 0, 0, 0)
time.sleep(.1)
win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)

#loop_time = time.time()

while True:
    screenshot = window_cap.window_cap_func(window_start_x, window_start_y)
    #color = screenshot[106, 55]
    #print("B: {}, G: {}, R: {}".format(color[0], color[1], color[2]))
    #cv.drawMarker(screenshot, (47, 105), color = (255, 0, 255), markerType = cv.MARKER_CROSS, markerSize = 5, thickness = 1)
    cv.imshow('osu!taiko bot', img)

    key_actions.play_taiko(screenshot)

    #print('FPS: {}'.format( 1 / (time.time() - loop_time)))
    #loop_time = time.time()

    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done')