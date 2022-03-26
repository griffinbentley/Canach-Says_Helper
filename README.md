# Canach-Says

Python based application made to help the player in a version of a memory game in the MMORPG Guild Wars 2 by ArenaNet.
Uses pyautogui and cv2 to take screenshots of the game and then uses image comparison to tell which symbol is being displayed to the player.
Uses time library to print key commands with precise timing, to minimize time loss.

When program is run, the program will begin to minotor keypresses. Before pressing 'F' for the first time, gather four charges for your jade bot. Press 'F' on an 'Expert "Canach Says" Console' in game, and the program will use precise timings to take a screenshot at the correct time to be able to record which symbol was displayed.
Using this information, the program then prints to the console which key the user should press in which order and at what time.

After the user finishes one game, the program will tell the player to press 'F' again to start another game.
Once four games have been played and the players' charges have been depleted, the program pauses and lets the player know that they need to gather more charges.
Once the player has four charges again, going up to an 'Experct "Canach Says" Console' and pressing 'F' will restart the program and allow the user to play another four games.