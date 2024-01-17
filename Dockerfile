# Configures a Flask web server and copies the current folder content
# to use as app root.

# Use the following commands to build and run the server.
#   docker build -t flask-server .
#   docker run -d -p 5000:5000 --name=flask-server flask-server

# Then open a web browser and connect to http://localhost:5000 .

# References:
#   https://code.visualstudio.com/docs/containers/quickstart-python
#   https://aka.ms/vscode-docker-python
#   https://runnable.com/docker/python/dockerize-your-flask-application
#   https://docs.docker.com/develop/develop-images/dockerfile_best-practices/

FROM python:alpine
RUN python -m pip install flask

WORKDIR /usr/src/app
COPY . .

EXPOSE 5000

CMD ["python", "app.py"]