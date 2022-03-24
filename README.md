# Canach-Says

Python based application made to help the player in a version of a memory game in the MMORPG Guild Wars 2 by ArenaNet.
Uses keyboard library to keylog the buttons used when the player plays the game, and builds a list of the symbols in order, so that it can tell the player the correct order.
Uses time library to print key commands with precise timing, to minimize time loss.

When program is run, press 'F' on an 'Expert "Canach Says" Console' in game, and the program will begin monitoring keystrokes to record the symbol list. As the player continouously
adds the newest symbol, it is appended to the list and then printed at the appropriate time later. After the game is won, the program will reset once the player presses 'F'
to start another game.
