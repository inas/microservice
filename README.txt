To run services:
docker-compose up --build

control + c to stop containers

register candidates: ex add candidate with ID candidate1:
curl -d '' http://0.0.0.0:5000/add/candidate1

see all registered candidates and the voters:
http://0.0.0.0:5000/

see candidates leaderboard:
http://0.0.0.0:5002/

vote for candidate: ex voter1 vote for candidate1:
curl -d '' http://0.0.0.0:5001/candidate1/voter1

reset voting, remove all candidates:
http://0.0.0.0:5003/
