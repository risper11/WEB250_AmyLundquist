# Displays "Hello world!"
#
# References:
#   https://en.wikiversity.org/wiki/Flask/Hello_World

import flask

app = flask.Flask(__name__)

@app.route('/')
def show_root():
    return "Hello world!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)