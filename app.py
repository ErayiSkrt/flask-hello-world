from flask import Flask
from flask_cors import  CORS
app = Flask(__name__)
CORS(app)

events = [{"eventName": "dragon"}]

characters = [];

@app.route('/loadEvents')
def sendEvents():
    return events

@app.route("/loadCharacters")
def sendCharacters():
    return characters

@app.route("/addCharacter/<charName>")
def addCharacter(charName):
    for name in characters:
        if name == charName:
            return;
    characters.append({"charName": charName});

if __name__ == "__main__":
    app.run()