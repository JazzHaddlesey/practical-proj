from application import app
from random import randint

@app.route('/get_nums', methods = ['GET'])
def get_nums():
    nums = randint(1, 179)
    return str(nums)
