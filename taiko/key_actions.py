import win32api, win32con

#Key 'a' Keycode is	65                  ####    COLORS    ####
#Key 's' keycode is 83                  # background circle G color = 51
#Key 'd' Keycode is	68                  # small red note B color = 44 G color = 69 R color = 235
#Key 'f' keycode is 70                  # small blue note B color = 172 G color = 142 R color = 67
#Key 'Space' keycode 32                 # big red note B color = 23 G color = 35 R color = 121 
#Key 'j' keycode is 74                  # big blue note B color = 88 G color = 73 R color = 34                 
#Key 'k' keycode is 75                  # 55, 110 pos for yellow bar?
#Key 'l' keycode is 76
#Key ';' keycode is 59

# By default all presses are actually holds
def key_press(key):

    if key == 'd':
        win32api.keybd_event(68, 0, 0, 0)

    elif key == 'f':
        win32api.keybd_event(70, 0, 0, 0)

    elif key == 'j':
        win32api.keybd_event(74, 0, 0, 0)

    elif key == 'k':
        win32api.keybd_event(75, 0, 0, 0)

def key_release(key):

    if key == 'd':
        win32api.keybd_event(68, 0, win32con.KEYEVENTF_KEYUP, 0)

    elif key == 'f':
        win32api.keybd_event(70, 0, win32con.KEYEVENTF_KEYUP, 0)
    
    elif key == 'j':
        win32api.keybd_event(74, 0, win32con.KEYEVENTF_KEYUP, 0)

    elif key == 'k':
        win32api.keybd_event(75, 0, win32con.KEYEVENTF_KEYUP, 0)


def play_taiko(screenshot):
    
    # Pixel pos for small notes
    # KEEP IN MIND THESE ARE Y AND X
    pixel_color_small = screenshot[106, 63] 
    pixel_color_failsafe = screenshot[105, 47]
    pixel_color_big = screenshot[62, 1]

    key_release('d')
    key_release('f')
    key_release('j')
    key_release('k')

    # Checks if the R color of the lowest possible pixel changes 
    # To something larger than the given RED threshold 
    # If true that means a small red note is present and presses corresponding buttons
    # The failsafe exists in case the note passes through the initial check pixel
    # With out triggering the button press
    if (pixel_color_small[2] > 150 or pixel_color_failsafe[2] > 150):
        key_press('f')

    # Same logic as small red notes but for blue notes
    # Checks for B color instead of R color
    if(pixel_color_small[0] >= 119 or pixel_color_failsafe[0] > 119):
        key_press('d')

    # Checks if the leftmost possible pixel changes to the given R value
    # If true that means a big red note is present and presses the corresponding buttons
    if(pixel_color_big[2] == 121):
        key_press('f')
        key_press('j')

    # Same logic as big red notes but for big blue notes
    # Checks for B color instead of R color
    if(pixel_color_big[0] == 88):
        key_press('d')
        key_press('k')