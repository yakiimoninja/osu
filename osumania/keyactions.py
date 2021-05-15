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
# Frame: as in every picture of the OPENCV stream
# Pixel pos X: to apply to the logic below
# Key: The key that will be pressed if all conditions are met
def action(frame, pixel_pos_x, difficulty, key,):
    
    # Upmost pixel of purple game bar B color = 155 at Y: 30
    frame_color = frame[30, pixel_pos_x]

    # Upmost pixel of long notes Y: 9
    frame_color_up = frame[9, pixel_pos_x]
    #print(frame_color)


    # Checks if the B value of the pixel is the same color as the upmost pixel color of the purple game bar
    # If it isnt the same color that means that there is a note present
    if frame_color[1] != 155:

        # This is for single notes
        # If the pixel isnt the same B color as the top pixel of the PURPLE game bar
        # Then it presses the corresponding button 
        key_press(key)
        
        # This is for long notes
        # If after press * (there is a tail, keep holding the button)
        # * the pixel at Y: 9 isnt the same B color as the background
        # Then keep holding the button  
        if frame_color_up[1] != 0:
            key_press(key)

    # frame_color[1] == 155 -> Checks if the B color of pixel is the same as the upmost pixel of the game bar
    # If its true that means that there isnt a single note present
    # frame_color_up[1] == 0 -> Checks if the B color of the pixel is the same color as the background
    # If its true that means that there isnt a long note present either
    # If both are true then we release the button press
    elif (frame_color[1] == 155 and frame_color_up[1] == 0):
        key_release(key)