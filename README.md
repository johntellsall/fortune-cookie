# hello
tiny Python project, for testing Docker and other tools

# run in Docker container

1. build image

`docker build -t hello-app .`

2. run container, mapping internal port

`docker run -it --rm -p 8000:8000 hello-app`

3. open browser to the container's exposed port

`open http://$(docker-machine ip default):8000`
