fetch("../../config.json").then(
    (res) => {
        if (res.ok) {
            let config = res.json();

            console.log(config.steam_id)
            document.getElementById("steam_input").value = config.steam_id
        }
        else {
            console.error("Something went wrong: " + res.status)
        }
    }
)