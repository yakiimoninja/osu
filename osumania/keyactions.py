import win32api
import win32con

#Key 'a' Keycode is	65
#Key 's' keycode is 83
#Key 'd' Keycode is	68
#Key 'f' keycode is 70
#Key 'Space' keycode 32
#Key 'j' keycode is 74
#Key 'k' keycode is 75
#Key 'l' keycode is 76
#Key ';' keycode is 59

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

def action(frame, pixel_pos_x, difficulty, key,):
    
    pixel_pos_y = 35 #BEST SO FAR 35
    #bar_color = [177, 91, 110]
    
    frame_color = frame[pixel_pos_y, pixel_pos_x]
    frame_color_up = frame[9, pixel_pos_x]
    #print(frame_color)


    #Checks if the B value of the pixel isnt the same color as the game hint bar
    if frame_color[1] != 91:

        #Button press
        key_press(key)
        
        if frame_color_up[1] != 0:
            key_press(key)
        #if frame_color_up[1] == 0:
        #    key_release(key)

        #print('Pressed ' + key)
    elif (frame_color[1] == 91 and frame_color_up[1] == 0):
        key_release(key)