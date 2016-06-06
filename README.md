# hello
tiny Python project, for testing Docker and other tools

# OSX Installation

```
brew install fortune
```

# run in Docker container

1. build image

`docker build -t hello-app .`

2. run container

`docker run -it --rm --name hello-proc hello-app`

3. open browser to the container's exposed port

`open http://localhost:8000/`
