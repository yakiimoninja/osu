import win32ui, win32gui, win32con
import numpy as np

#Calling Windows API for higher fps capture
def window_cap_func(x, y):

    hwnd = win32gui.FindWindow(None, "osu!")

    w = 251
    h = 125

    # Removing unused capture space
    cropped_x = x + 241
    cropped_y = y + 333

    wDC = win32gui.GetWindowDC(hwnd)
    dcObj = win32ui.CreateDCFromHandle(wDC)
    cDC = dcObj.CreateCompatibleDC()
    dataBitMap = win32ui.CreateBitmap()
    dataBitMap.CreateCompatibleBitmap(dcObj, w, h)
    cDC.SelectObject(dataBitMap)
    cDC.BitBlt((0, 0), (w, h), dcObj, (cropped_x, cropped_y), win32con.SRCCOPY)

    # Save screenshot to file
    # dataBitMap.SaveBitmapFile(cDC, 'debug.bmp')

    signedIntsArray = dataBitMap.GetBitmapBits(True)
    img = np.fromstring(signedIntsArray, dtype = 'uint8')
    img.shape = (h, w, 4)

    # Free Resources
    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())

    #Gets rid of alpha channel, dont use if not matchtemplate
    #img = img[...,:3]
    #For the error with draw rectangles
    #img = np.ascontiguousarray(img)

    return img

# This gets the top left coordinates of the window
def window_tracking(coordinate):
    
    hwnd = win32gui.FindWindow(None, "osu!")
    window_pos = win32gui.GetWindowPlacement(hwnd)
    # Logic to isolate the X and Y
    window_pos = window_pos[4]
    window_start_x = window_pos[0]
    window_start_y = window_pos[1]
    
    if coordinate == 'x':
        return window_start_x
    if coordinate == 'y':
        return window_start_y