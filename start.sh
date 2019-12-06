kubectl apply -f redis-deployment.yaml
kubectl apply -f redis-service.yaml

kubectl apply -f reset-deployment.yaml
kubectl apply -f reset-service.yaml
kubectl expose deployment reset --type=LoadBalancer --name=reset-lb

#kubectl apply -f reset-deployment.yaml
#kubectl apply -f redis-service.yaml