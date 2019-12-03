import json

import requests
from flask import Flask, make_response
from redis import Redis

app = Flask(__name__)
db = Redis(host='redis', port=6379)


@app.route('/')
def get_leaderboard():
    header_content = {'Content-type': 'application/json'}
    response = requests.get("http://192.168.0.5:5000/", headers=header_content).json()
    result = {}
    for key in sorted(response, key=lambda k: len(response[k]), reverse=True)[:10]:
        result[key] = db.llen(key) - 1

    response = make_response(json.dumps(result, indent=4))
    response.headers['Content-type'] = "application/json"
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)
