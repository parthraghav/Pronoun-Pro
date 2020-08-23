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
    text_delimiter = ' This is a delimiter. '
    result = ""
    if request.method == 'POST':
        data_map = request.json['data']
        try:
            text = text_delimiter.join(
                [data_map[key] for key in sorted(data_map.keys())])
            output = neutralise(text)
            result = {
                str(index): val
                for index, val in enumerate(output.split(text_delimiter))
            }
            status = ServerResponse.SUCCESS
        except:
            status = ServerResponse.FAILURE
    return jsonify({'status': str(status.value), 'result': result})


if __name__ == '__main__':
    app.run()