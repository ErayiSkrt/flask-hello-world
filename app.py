from flask import Flask
app = Flask(__name__)

events = ["dragon"];

characters = [];

@app.route('/loadEvents')
def sendEvents():
    return events

@app.route("/loadCharacters")
def sendCharacters():
    return characters

@app.route("/addCharacter")
def addCharacter(charName):
    characters.append(charName);
    return sendCharacters();


if __name__ == "__main__":
    app.run()