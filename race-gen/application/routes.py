from application import app
from flask import render_template, request


@app.route('/get_race', methods = ['GET'])
def get_race():
    data_sent = request.get_json()
    if data_sent['nums'] > 0 and data_sent['nums'] < 20:
        return "Dwarf"
    elif data_sent['nums'] >= 21 and data_sent['nums'] < 40:
        return "Elf"
    elif data_sent['nums'] >= 41 and data_sent['nums'] < 60:
        return "Hafling"
    elif data_sent['nums'] >= 61 and data_sent['nums'] < 80:
        return "Human"
    elif data_sent['nums'] >= 81 and data_sent['nums'] < 100:
        return "Dragonborn"
    elif data_sent['nums'] >= 101 and data_sent['nums'] < 120:
        return "Gnome"
    elif data_sent['nums'] >= 121 and data_sent['nums'] < 140:
        return "Half-Elf"
    elif data_sent['nums'] >= 141 and data_sent['nums'] < 160:
        return "Half-Orc"
    elif data_sent['nums'] >= 161 and data_sent['nums'] < 180:
        return "Tiefling"
        
