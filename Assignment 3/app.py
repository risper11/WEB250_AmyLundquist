# Converts a Fahrenheit temperature to Celsius using a GET request and
# converts a Celsius temperature to Fahrenheit using a POST request.
#
# References:
#   https://www.mathsisfun.com/temperature-conversion.html
#   https://en.wikibooks.org/wiki/Python_Programming
#   https://www.digitalocean.com/community/tutorials/processing-incoming-request-data-in-flask

import flask

app = flask.Flask(__name__)

GET_FORM = """
<form method="GET">
<label for="fahrenheit">Enter Fahrenheit temperature:</label>
<input type="text" id="fahrenheit" name="fahrenheit">
<input type="submit" value="Submit">
</form>
"""

EMPTY_PARAGRAPH = """
<p>&nbsp;</p>
"""

POST_FORM = """
<form method="POST">
<label for="celsius">Enter Celsius temperature:</label>
<input type="text" id="celsius" name="celsius">
<input type="submit" value="Submit">
</form>
"""

@app.route('/', methods=["GET"])
def root_get():
    return process_get_request()

@app.route('/', methods=["POST"])
def root_post():
    return process_post_request()

def process_get_request():
    request = flask.request
    result = GET_FORM

    try:
        fahrenheit = float(request.args["fahrenheit"])
        celsius = (fahrenheit - 32) * 5 / 9
        result += "<p>" + str(fahrenheit) + "° Fahrenheit is " + \
            str(celsius) + "° Celsius</p>"
    except:
        result += EMPTY_PARAGRAPH
    
    result += POST_FORM + EMPTY_PARAGRAPH
    return result

def process_post_request():
    request = flask.request
    result = GET_FORM + EMPTY_PARAGRAPH + \
        POST_FORM

    try:
        celsius = float(request.form["celsius"])
        fahrenheit = celsius * 9 / 5 + 32
        result += "<p>" + str(celsius) + "° Celisus is " + \
            str(fahrenheit) + "° Fahrenheit</p>"
    except:
        result += EMPTY_PARAGRAPH

    return result

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)