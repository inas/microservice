kubectl autoscale deployment candidates --cpu-percent=50 --min=1 --max=10
kubectl autoscale deployment vote --cpu-percent=50 --min=1 --max=10
kubectl autoscale deployment leaderboard --cpu-percent=50 --min=1 --max=10
kubectl autoscale deployment reset --cpu-percent=50 --min=1 --max=10

