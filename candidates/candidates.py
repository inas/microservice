import json

from flask import Flask, make_response
from redis import Redis

app = Flask(__name__)
db = Redis(host='redis', port=6379)


@app.route('/', methods=['GET'])
def get_candidates():
    result = {}
    if db.dbsize() > 0:
        for candidate in db.keys():
            candidate = candidate.decode('utf-8')
            result[candidate] = []
            for voter in db.lrange(candidate, 0, -1):
                result[candidate].append(voter.decode('utf-8'))

    response = make_response(json.dumps(result, indent=4))
    response.headers['Content-type'] = "application/json"
    return response


@app.route('/add/<candidate_id>', methods=['POST'])
def add_candidate(candidate_id):
    result = {}
    if db.exists(candidate_id):
        result['result'] = 'Candidate with ID of %s already exists' % candidate_id
    else:
        db.lpush(candidate_id, "")
        result['result'] = 'Candidate with ID %s is added' % candidate_id

    response = make_response(json.dumps(result, indent=4))
    response.headers['Content-type'] = "application/json"
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
