import win32ui, win32gui, win32con
import numpy as np

#Calling Windows API for higher fps capture
def window_cap_func(x, y):

    hwnd = win32gui.FindWindow(None, "osu!")

    w = 394 #1920#
    h = 50 #1080#

    # Removing unused capture space
    cropped_x = x + 258
    cropped_y = y + 750

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