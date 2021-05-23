import win32api, win32con

#Key 'a' Keycode is	65                  ####    COLORS    ####
#Key 's' keycode is 83                  # purple game bar B color = 91
#Key 'd' Keycode is	68                  # upmost purple game bar G color = 155
#Key 'f' keycode is 70                  # green note G color = 186
#Key 'Space' keycode 32                 # purple note G color = 69
#Key 'j' keycode is 74
#Key 'k' keycode is 75
#Key 'l' keycode is 76
#Key ';' keycode is 59

# By default all presses are actually holds
def key_press(key):

    if key == 'a':
        win32api.keybd_event(65, 0, 0, 0)
    
    elif key == 's':
        win32api.keybd_event(83, 0, 0, 0)
    
    elif key == 'd':
        win32api.keybd_event(68, 0, 0, 0)

    elif key == 'f':
        win32api.keybd_event(70, 0, 0, 0)
    
    elif key == 'space':
        win32api.keybd_event(32, 0, 0, 0)

    elif key == 'j':
        win32api.keybd_event(74, 0, 0, 0)

    elif key == 'k':
        win32api.keybd_event(75, 0, 0, 0)

    elif key == 'l':
        win32api.keybd_event(76, 0, 0, 0)

    elif key == ';':
        win32api.keybd_event(59, 0, 0, 0)

def key_release(key):

    if key == 'a':
        win32api.keybd_event(65, 0, win32con.KEYEVENTF_KEYUP, 0)

    elif key == 's':
        win32api.keybd_event(83, 0, win32con.KEYEVENTF_KEYUP, 0)
    
    elif key == 'd':
        win32api.keybd_event(68, 0, win32con.KEYEVENTF_KEYUP, 0)

    elif key == 'f':
        win32api.keybd_event(70, 0, win32con.KEYEVENTF_KEYUP, 0)
    
    elif key == 'space':
        win32api.keybd_event(32, 0, win32con.KEYEVENTF_KEYUP, 0)

    elif key == 'j':
        win32api.keybd_event(74, 0, win32con.KEYEVENTF_KEYUP, 0)

    elif key == 'k':
        win32api.keybd_event(75, 0, win32con.KEYEVENTF_KEYUP, 0)

    elif key == 'l':
        win32api.keybd_event(76, 0, win32con.KEYEVENTF_KEYUP, 0)

    elif key == ';':
        win32api.keybd_event(59, 0, win32con.KEYEVENTF_KEYUP, 0)


# OSU MANIA GAME LOGIC
# This function takes arguments
# Frame: as in every picture of the video stream
# Pixel pos X: to apply to the logic below
# Key: The key that will be pressed if all conditions are met
def logic(frame, pixel_pos_x, key,):
    
    # Upmost pixel of purple game bar G color = 155 at Y: 30
    # G Color of purple game bar = 91 at Y: 31
    frame_color_long = frame[30, pixel_pos_x]
    frame_color_single = frame[26, pixel_pos_x]
    # Upmost pixel of long notes Y: 9
    frame_color_up = frame[9, pixel_pos_x]
    

    # Checks if the G value of the pixel is the same color as G color of the single note
    # If it is the same color that means that there is a note present and presses the respective button
    if frame_color_single[1] == 69:
        key_press(key)

    # Checks if the G value of the pixel is the same color as G color of the long note
    elif frame_color_long[1] == 186:
        key_press(key)

    # frame_color_long[1] == 155 -> Checks if the G color of the pixel is the same as the upmost pixel of the game bar
    # If its true that means that there isnt a single note present
    # frame_color_up[1] == 0 -> Checks if the G color of the pixel is the same color as the background
    # If its true that means that there isnt a long note present either
    # If both are true then we release the button press
    elif (frame_color_long[1] == 155 and frame_color_up[1] == 0):
        key_release(key)

def play_mania(dif, screenshot):

    if dif == 4:
        
        logic(screenshot, 35, 'd')
        logic(screenshot, 85, 'f')
        logic(screenshot, 140, 'j')
        logic(screenshot, 200, 'k')
        
    if dif == 5:
        logic(screenshot, 35, 'd')
        logic(screenshot, 85, 'f')
        logic(screenshot, 140, 'space')
        logic(screenshot, 200, 'j')
        logic(screenshot, 250, 'k')
        
    if dif == 6:
        logic(screenshot, 35, 's')
        logic(screenshot, 85, 'd')
        logic(screenshot, 140, 'f')
        logic(screenshot, 200, 'j')
        logic(screenshot, 250, 'k')
        logic(screenshot, 315, 'l')

    if dif == 7:
        logic(screenshot, 35, 's')
        logic(screenshot, 85, 'd')
        logic(screenshot, 140, 'f')
        logic(screenshot, 200, 'space')
        logic(screenshot, 250, 'j')
        logic(screenshot, 315, 'k')
        logic(screenshot, 365, 'l')
