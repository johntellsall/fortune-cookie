# hello
tiny Python project, for testing Docker and other tools

# run in Docker container

1. build image

`docker build -t hello-app .`

2. run container, mapping internal port to outside

`docker run -it --rm -P hello-app`

3. open browser to the container's outside port

`open http://$(docker-machine ip default):8000`
