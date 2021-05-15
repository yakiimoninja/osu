import win32ui, win32gui, win32con
import numpy as np

class WindowCapture:
    
    #Properties
    w = 0 
    h = 0
    cropped_x = 0
    cropped_y = 0
    offset_x = 0
    offset_y = 0
    hwnd = None

    #Constructor
    def __init__(self):
        
        self.w = 655
        self.h = 800
        self.hwnd = None

        #Removing unused capture space
        sidepx = 250
        toppx = 750

        self.w = self.w - sidepx
        self.h = self.h - toppx

        self.cropped_x = sidepx
        self.cropped_y = toppx


    #Calling Windows API for higher fps capture
    def window_cap_func(self):

        wDC = win32gui.GetWindowDC(self.hwnd)
        dcObj = win32ui.CreateDCFromHandle(wDC)
        cDC = dcObj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, self.w, self.h)
        cDC.SelectObject(dataBitMap)
        cDC.BitBlt((0, 0), (self.w, self.h), dcObj, (self.cropped_x, self.cropped_y), win32con.SRCCOPY)

        #Save screenshot to file
        # dataBitMap.SaveBitmapFile(cDC, 'debug.bmp')

        signedIntsArray = dataBitMap.GetBitmapBits(True)
        img = np.fromstring(signedIntsArray, dtype = 'uint8')
        img.shape = (self.h, self.w, 4)

        # Free Resources
        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(self.hwnd, wDC)
        win32gui.DeleteObject(dataBitMap.GetHandle())

        #Gets rid of alpha channel, dont use if not matchtemplate
        #img = img[...,:3]
        #For the error with draw rectangles
        #img = np.ascontiguousarray(img)

        return img