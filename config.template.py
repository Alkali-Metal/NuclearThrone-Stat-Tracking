# This is your Steam 64ID, can be found by entering your account URL
#  at this (https://steamid.io/) website and copying the "steamID64" result
steam_ID = ""



# This is the stream key from the game itself, found by going to:
#  Settings --> Game
# and hitting the "Stream Key" option and entering the code perfectly.
game_stream_ID = ""
# NOTE: you must enable the stream key every time you play in the game
#       when you want this program running, but you only need to enter
#       the code once as it's always the same.





# This will tell the software to log pretty major things to plaintext files
#  in the stats/ directory so that you could have something like OBS reading
#  from that file for a livestream overlay or something.
live_logging = True

# This indicates whether or not to condense all of the live stats into a single
#  condensed.txt file
condense_live_stats = False # NOT IMPLEMENTED YET

# This indicates what files will store which data and which events we should be
#  logging. To remove a datapoint, just comment it out by adding a "#" in front
#  of key/value pair
live_events = {
    "charlvl": "stats/char_level.txt",
    "kills": "stats/kills.txt",
    "wepA": "stats/wepA.txt",
    "wepB": "stats/wepB.txt",
    "loops": "stats/total_loops.txt"
}


# This determines what format the program will output data in, this can be
#  either:
#
#  "json" - Logs in a JSON format, useful for Microsoft Excel.
#  "csv" NOT IMPLEMENTED YET - Logs in a CSV format, useful for LibreOffice Calc.
output_type = "json"