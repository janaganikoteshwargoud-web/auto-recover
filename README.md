# Auto-Recover - Self Healing App

Docker --restart always tho app crash ayina malli auto ga start avthundi.

## Run
docker build -t auto-recover .
docker run -d --name myapp --restart always -p 5000:5000 auto-recover

## Test
curl localhost:5000
curl localhost:5000/crash
docker ps
