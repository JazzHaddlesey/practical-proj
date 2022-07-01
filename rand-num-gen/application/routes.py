from application import app
from flask import render_template
from random import randint

@app.route('/get_num', methods = ['GET'])
def num_gen():
    nums = randint(0, 180)
    return str(nums)
