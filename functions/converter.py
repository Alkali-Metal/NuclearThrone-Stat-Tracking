from time import time

import functions.game_data as GD

def ID_to_string(datapoint, ID):
    if hasattr(GD, datapoint):
        return getattr(GD, datapoint)[ID]



def JSON(data):
    response = {}

    if data:
        response["timestamp"] = data["timestamp"]
        response["loops"] = data["loops"]
        response["kills"] = data["kills"]


        response["character"] = GD.character_IDs[data["char"]]
        response["char_lvl"] = data["charlvl"]


        response["weapon_a"] = GD.weapon_IDs[data["wepA"]]
        response["weapon_b"] = GD.weapon_IDs[data["wepB"]]


        response["crown"] = GD.crown_IDs[data["crown"]]


        response["level"] = data["level"]
        response["world"] = "{}({})".format(
            GD.world_IDs[data["world"]],
            data["world"]
        )


        # Check if they died or quit the game
        if data["health"] == 0:
            response["killed_by"] = GD.enemy_IDs[data["lasthit"]]
        else:
            response["killed_by"] = "Exited game"


        #"0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0"
        #"28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9  8  7  6  5  4  3  2  1  0"
        bit_index = 28
        response["mutations"] = []
        for mutation in data["mutations"]:
            if mutation == "1":
                response["mutations"].append(GD.mutation_IDs[bit_index])
            bit_index -= 1

        return response