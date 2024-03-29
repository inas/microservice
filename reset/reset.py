from flask import Flask
from redis import Redis

app = Flask(__name__)
db = Redis(host='redis', port=6379)


@app.route('/', methods=['POST'])
def hello_world():
    db.flushdb()
    return 'Reset voting. Number of candidates is now: %s\n' % db.dbsize()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003, debug=True)
