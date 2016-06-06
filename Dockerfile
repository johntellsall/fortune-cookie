# 1. build image	docker build -t my-python-app .
# 2. run container	docker run -it --rm --name my-running-app my-python-app
# 3. open browser to http://localhost:8000/

FROM python:2-onbuild

EXPOSE 8000
CMD [ "python", "./hello.py" ]
