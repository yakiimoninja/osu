# This checks how many keys are present
# Does that by checking how long the purple game bar is
# Checks if the B color of the game bar exists
# At the locations of the 5th, 6th, 7th key
def dif_check(screenshot):

    screenshot_4 = screenshot[35, 200]
    screenshot_5 = screenshot[35, 250]
    screenshot_6 = screenshot[35, 315]
    screenshot_7 = screenshot[35, 365]

    if screenshot_7[1] == 91:
        return 7
    elif screenshot_6[1] == 91:
        return 6
    elif screenshot_5[1] == 91:
        return 5
    elif screenshot_4[1] == 91:
        return 4