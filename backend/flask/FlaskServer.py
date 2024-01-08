from flask import Flask, jsonify
from flask_cors import CORS


# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})
# # CORS(app, resources={r"/*":{'origins': 'http://localhost:5000', "allow_headers":"Access-Control-Allow-Origin"}})

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


# hello world route
@app.route('/', methods=['GET'])
def greetings():
  return "Hello world!"


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True, port=5000)