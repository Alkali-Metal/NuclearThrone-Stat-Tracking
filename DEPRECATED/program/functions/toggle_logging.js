var is_logging = false;

// Toggle whether or not we are logging the data
const toggle_logging = () => {

    var running = false,
        steam_id = document.getElementById("steam_id")[0].value,
        game_id = document.getElementById("game_id")[0].value;


    // Time to yell at the user
    if (!steam_id || !game_id) {
        return alert("You must specify a value for Steam ID and Stream Key!")
    };


    // We better go and catch the logger!
    if (running) {
        clearInterval();
        running = false;
    }

    // Let's give the logger a bit of a shove to get it going
    else {
        setInterval(
            () => {

                // Get the data from the API
                let response = axios.get(
                    Config.API_url + `?s=${steam_id}&key=${game_id}`
                )
            },
            1000
        );
        running = true;
    };
};