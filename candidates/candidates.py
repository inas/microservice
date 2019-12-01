from flask import Flask
from redis import Redis

app = Flask(__name__)
db = Redis(host='redis', port=6379)


@app.route('/')
def hello_world():
    db.decr('count')
    return 'CANDIDATES Count is %s.' % db.get('count')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
