from flask import Flask
from flask_cors import  CORS
app = Flask(__name__)
CORS(app)

events = [{"eventName": "dragon"}]

characters = [{"charName": "testName"}];

@app.route('/loadEvents')
def sendEvents():
    return events

@app.route("/loadCharacters")
def sendCharacters():
    return characters

@app.route("/addCharacter/<charName>")
def addCharacter(charName):
    for name in characters:
        if name["charName"] == charName:
            return {"0":"character already exists"};

    characters.append({"charName": charName});
    return {"0":"character added", "1":"adding"}

@app.route("/removeCharacter/<charName>")
def removeCharacter(charName):
    global characters;
    updatedList = [d for d in characters if d.get("charName") != charName]
    if len(updatedList) < len(characters):
        characters = updatedList;
        return {"0":"character removed", "1": "removed"};

    return {"0":"character with name " + charName + " does not exist"};

if __name__ == "__main__":
    app.run()