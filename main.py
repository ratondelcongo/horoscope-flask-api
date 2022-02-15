from unittest import result
from flask import Flask
from flask import jsonify
from flask import request
from utils import ZODIAC_NUMBERS
from utils import ZODIAC_NAMES
from utils import get_horoscope

def create_app():
    app = Flask(__name__)
    return app

app = create_app()

@app.route("/")
def hello_world():
    return "<p>xd!</p>"

@app.route('/api/v1/horoscope', methods=['GET'])
def get_users():
    args = request.args
    sign = args.get("sign")
    result = get_horoscope(sign)
    response = {'result': result}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)