from functions.converter import ID_to_string

import config


datapoints = {
    "charlvl": "raw",
    "kills": "raw",
    "wepA": "convert",
    "wepB": "convert",
    "loops": "raw",
    "crown": "convert",
    "char": "convert"
}

datatypes = {
    "wepA": "weapon_IDs",
    "wepB": "weapon_IDs",
    "crown": "crown_IDs",
    "char": "character_IDs"
}

text_format = {
    "charlvl": "Char Lvl:\n          {}",
    "kills": "Kills: {}",
    "wepA": "Weapon 1:\n   {}",
    "wepB": "Weapon 2:\n   {}",
    "loops": "Loops: {}",
    "crown": "Crown:\n  {}",
    "char": "Character:\n  {}"
}


def update_txt(data):

    # Cycle through all events user wants to update
    for key, path in config.live_events.items():

        # Ensure key exists in the data given to us from NT
        if key in data:

            # Ensure that we know what to do with the given datapoint
            if key in datapoints:

                # See if we need to convert it
                if datapoints[key] == "convert":
                    value = ID_to_string(datatypes[key], data[key])
                
                # See if we are leaving the value alone
                elif datapoints[key] == "raw":
                    value = data[key]
                
                with open(path, "w+") as file:
                    file.write(text_format[key].format(value))
            
            # Error as we don't know what to do with datapoint
            else:
                print("I can't update '{}' as I don't know what to do with it.".format(key))