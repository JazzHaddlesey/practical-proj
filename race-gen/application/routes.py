from application import app
from flask import request


@app.route('/get_race', methods = ['POST'])
def get_race():
    data_sent = request.get_json()
    int_data = int(data_sent['nums'])
    if int_data > 0 and int_data < 20:
        return str("Dwarf")
    elif int_data >= 21 and int_data < 40:
        return str("Elf")
    elif int_data >= 41 and int_data < 60:
        return str("Hafling")
    elif int_data >= 61 and int_data < 80:
        return str("Human")
    elif int_data >= 81 and int_data < 100:
        return str("Dragonborn")
    elif int_data >= 101 and int_data < 120:
        return str("Gnome")
    elif int_data >= 121 and int_data < 140:
        return str("Half-Elf")
    elif int_data >= 141 and int_data < 160:
        return str("Half-Orc")
    elif int_data >= 161 and int_data < 180:
        return str("Tiefling")
    # elif int_data >= 181 and int_data < 200:
    #     return str("Centaur")
    # elif int_data >= 201 and int_data < 220:
    #     return str("Changeling")
    # elif int_data >= 221 and int_data < 240:
    #     return str("Fairy")
    # elif int_data >= 241 and int_data < 260:
    #     return str("Eladrin")
    # elif int_data >= 261 and int_data < 280:
    #     return str("Goliath")
    

        
