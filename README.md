# fortune-cookie
tiny Python project, for testing Docker and other tools

# run in Docker container (app only)

1. build image

`docker build -t fortune-app .`

2. run container, mapping internal port to outside

`docker run -it --rm -P fortune-app`

3. open browser to the container's outside port

`open http://$(docker-machine ip default):8000`

# run in Compose cluster (app with HAProxy)

TBD
