import win32api
import win32con
import time as time

#Key 'a' Keycode is	65                  ####    COLORS    ####
#Key 's' keycode is 83                  # background circle G color = 51
#Key 'd' Keycode is	68                  # small red note B color = 44 G color = 69 R color = 235
#Key 'f' keycode is 70                  # small blue note B color = 172 G color = 142 R color = 67
#Key 'Space' keycode 32                 # big red note B color = 40 G color = 62 R color = 212 
#Key 'j' keycode is 74                  # big blue note B color = 155 G color = 128 R color = 60                 
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
    pixel_color_small = screenshot[106, 63] # KEEP IN MIND THESE ARE Y AND X
    pixel_color_big = screenshot[62, 1]

    key_release('d')
    key_release('f')
    key_release('j')
    key_release('k')

    if (pixel_color_small[2] >= 220):
        key_press('f')
        #print("pressed small red")
    if(pixel_color_small[0] >= 150):
        key_press('d')
        #print("pressed small blue")

    if(pixel_color_big[1] == 62 or pixel_color_big[1] == 69 or pixel_color_big[1] == 63 
    or pixel_color_big[1] == 64 or pixel_color_big[1] == 65 or pixel_color_big[1] == 66):
        key_press('f')
        key_press('j')
        #print("pressed big red")
    if(pixel_color_big[1] == 128):
        key_press('d')
        key_press('k')
        #print("pressed big blue")
    #else:
        #None
        #key_release('d')
        #key_release('f')
        #key_release('j')
        #key_release('k')
        #print("released all")