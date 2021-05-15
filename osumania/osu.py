import cv2 as cv
import time
import keyactions
from windowcap import WindowCapture


# OSU WINDOW SHOULD BE SET TO 1400 * 900 WINDOWED AND TOP LEFT CORNER FOR THIS TO WORK
wincap = WindowCapture()

#pos X 35, 85 140 200 250, 315, 365

time.sleep(3)

#loop_time = time.time()
while True:
    screenshot = wincap.window_cap_func()
    screenshot
    #cv.drawMarker(screenshot, (200, 9), color = (255, 0, 255), markerType = cv.MARKER_CROSS, markerSize = 1, thickness = 1)
    cv.imshow('Computer Vision', screenshot)

    keyactions.action(screenshot, 35, 4, 's')
    keyactions.action(screenshot, 85, 4, 'd')
    keyactions.action(screenshot, 140, 4, 'f')
    keyactions.action(screenshot, 200, 4, 'space')
    keyactions.action(screenshot, 250, 4, 'j')
    keyactions.action(screenshot, 315, 4, 'k')
    keyactions.action(screenshot, 365, 4, 'l')

    #print('FPS: {}'.format( 1 / (time.time() - loop_time)))
    #loop_time = time.time()

    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break


#first 0 - 50
print('Done')