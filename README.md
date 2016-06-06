# hello
tiny Python project, for testing Docker and other tools

# OSX Installation

```
brew install fortune
```

# run in Docker container

1. build image

`docker build -t my-python-app .`

2. run container

`docker run -it --rm --name my-running-app my-python-app`

3. open browser to http://localhost:8000/
