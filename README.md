# Bot that plays osu!mania and osu!taiko.


<p float="left">
  <img src="https://user-images.githubusercontent.com/80072600/119259630-a0bf3d00-bbbe-11eb-96c5-c0ce6019c89f.gif" width="362" height="620" />
  <img src="https://user-images.githubusercontent.com/80072600/119258685-5340d100-bbba-11eb-8a2a-5a7f9c6b6a75.gif" width="600" height="200" />
</p>

# General notes.
Game window must be set to ```1400 x 900``` and windowed for this to work.

Game window must not be moved after the lauch of the bot.

Skin assests provided must be used for this to work.

After running the bot you have 3 seconds to ```Alt + Tab``` to the game window.

The bot then will automatically press ```Enter``` to the map that is selected at the song list screen.

To terminate the bot hit the ```Q``` key on the bot window.

# Mania specific notes.
Unless you are going to play a beatmap with the same number of keys, you must restart the bot.

# Taiko specific notes.
If the bot misses notes, it's recommended to disable the UI by hitting ```Shift + Tab```.

# Usage and requirements.

This requires python3 and ```pip``` installing the ```opencv-python``` and ```pywin32``` packages.

To run the bot for osu!mania:
Move to the ```mania``` directory and run through cmd the command -> ```py mania.py```.

To run the bot for osu!taiko:
Move to the ```taiko``` directory and run through cmd the command -> ```py taiko.py```.
