from application import app
from flask import render_template
import requests

@app.route('/')
def index():
    name = requests.get('http://rand-name-gen:5000/get_name').text
    nums = requests.get('http://rand-num-gen:5000/get_nums').text
    race = requests.post('http://race-gen:5000/get_race', json = dict(nums = nums))
    return render_template('home.html', name = name, race = race.text)
