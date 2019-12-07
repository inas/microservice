import requests
from flask import Flask
from redis import Redis

app = Flask(__name__)
db = Redis(host='redis', port=6379)


@app.route('/<candidate_id>/<voter_id>', methods=['POST'])
def vote(candidate_id, voter_id):
    header_content = {'Content-type': 'application/json'}
    response = requests.get("http://candidates:5000/", headers=header_content).json()
    if candidate_id in response:
        db.lpush(candidate_id, voter_id)
        return '%s got your vote!\n' % candidate_id
    else:
        return 'Candidate with ID %s does not exists\n' % candidate_id

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
