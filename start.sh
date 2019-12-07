kubectl apply -f redis-deployment.yaml
kubectl apply -f redis-service.yaml

kubectl apply -f reset-deployment.yaml
kubectl apply -f reset-service.yaml
kubectl expose deployment reset --type=LoadBalancer --name=reset-lb

kubectl apply -f candidates-deployment.yaml
kubectl apply -f candidates-service.yaml
kubectl expose deployment candidates --type=LoadBalancer --name=candidates-lb

kubectl apply -f vote-deployment.yaml
kubectl apply -f vote-service.yaml
kubectl expose deployment vote --type=LoadBalancer --name=vote-lb

kubectl apply -f leaderboard-deployment.yaml
kubectl apply -f leaderboard-service.yaml
kubectl expose deployment leaderboard --type=LoadBalancer --name=leaderboard-lb

