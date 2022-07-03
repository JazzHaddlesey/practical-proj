from application import app
from random import randint

@app.route('/get_nums', methods = ['GET'])
def get_nums():
    nums = randint(0, 180)
    return str(nums)
