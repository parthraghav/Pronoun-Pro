from flask import Flask, request, jsonify
from flask_cors import CORS
from analyze import neutralise
import requests
from enum import Enum
app = Flask(__name__)
CORS(app)


class ServerResponse(Enum):
    SUCCESS = 200
    INVALID = 400
    FAILURE = 500


@app.route('/', methods=['POST'])
def serve_neutraliser():
    status = ServerResponse.INVALID
    result = ""
    if request.method == 'POST':
        text = request.json['data']
        try:
            result = neutralise(text)
            status = ServerResponse.SUCCESS
        except:
            status = ServerResponse.FAILURE
    return jsonify({'status': str(status.value), 'result': result})


if __name__ == '__main__':
    app.run()