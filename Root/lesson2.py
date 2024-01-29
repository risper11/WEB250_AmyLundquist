import flask
from datetime import datetime
date = datetime.now()
day = date.strftime("%m/%d/%Y")
time = date.strftime("%H:%M:%S")
url = request('host_url')
#ip = flask.request('remote_addr')
#os = flask.request.headers.get('User-Agent')


def main():
    data = {    
            "day": day,
            "time": time,
            "url": url,
            "ip": ip,
            "os": os
        }
    return flask.render_template('template.html', data=data)