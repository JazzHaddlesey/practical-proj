from application import app
import names

@app.route('/get_name', methods = ['GET'])
def get_name():
    full_name = names.get_full_name()
    return full_name
