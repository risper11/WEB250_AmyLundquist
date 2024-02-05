
import flask
from flask import request
from datetime import datetime
date = datetime.now()
day = date.strftime("%m/%d/%Y")
time = date.strftime("%H:%M:%S")
#url = flask.request.host_url
#url = flask.request.url
#ip = flask.request.remote_addr
#os = flask.request.headers.get('User-Agent')
#headers = request.headers

def main():
    data = {    
            "day": day,
            "time": time
            #"headers": headers
            #"url": url
            #"ip": ip,
           # "os": os
        }
    return flask.render_template('assignment2.html', data=data)