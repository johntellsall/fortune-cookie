FROM python:2-onbuild

RUN apt-get update && apt-get install -y fortune-mod

EXPOSE 8000
CMD [ "python", "./hello.py" ]
