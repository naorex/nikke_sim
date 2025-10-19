from flask import Flask

app = Flask(__name__)

nikke_character = {
    "SoldierEG": {"hp": 244350, "attack_power": 4805, "defence_power": 1837}
}


@app.route("/character/<string:name>", methods=["GET"])
def get_character(name):
    character = nikke_character.get(name)
    return character, 200


if __name__ == "__main__":
    app.run(debug=True)
