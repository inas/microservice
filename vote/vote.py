from flask import Flask
from redis import Redis

app = Flask(__name__)
db = Redis(host='redis', port=6379)


@app.route('/')
def hello_world():
    db.incr('count')
    return 'VOTE Count is %s.' % db.get('count')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
