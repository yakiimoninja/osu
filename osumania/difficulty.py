import cv2 as cv


def dif_check(frame):

    #THIS CHECKS FROM 4K DIFFICULTY TO 7K DIFFICULTY
    #Using a fixed Y we check the difficulty by measuring how many keys are present
    #We do that by matching the purple color of the bar above the keys to the background color
    #If its purple through out these fixed X positions we know determine the difficulty

    #pos X 35, 85 140 200 250, 315, 365

    pixel_y = 35
    x_pos_5 = 250
    x_pos_6 = 315
    x_pos_7 = 365

    if frame

    #==========TODO============#