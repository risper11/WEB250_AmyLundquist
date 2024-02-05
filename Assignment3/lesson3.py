# Converts a Fahrenheit temperature to Celsius using a GET request and
# converts a Celsius temperature to Fahrenheit using a POST request.
#
# References:
#   https://www.mathsisfun.com/temperature-conversion.html
#   https://en.wikibooks.org/wiki/Python_Programming
#   https://www.digitalocean.com/community/tutorials/processing-incoming-request-data-in-flask

import flask

app = flask.Flask(__name__)

#GET_FORM = """
#<form method="GET">
#<label for="fahrenheit">Enter Fahrenheit temperature:</label>
#<input type="text" id="fahrenheit" name="fahrenheit">
#<input type="submit" value="Submit">
#</form>
#"""

#POST_FORM = """
#<form method="POST">
#<label for="celsius">Enter Celsius temperature:</label>
#<input type="text" id="celsius" name="celsius">
#<input type="submit" value="Submit">
#</form>
#"""

EMPTY_PARAGRAPH = """
<p>&nbsp;</p>
"""

RECTANGLE_FORM = """
<h1 class="header3">Area Calculator</h1>
<form method="GET">
<h2 class="header3">Rectangle Area Calculator</h2>
<label for="length">Enter Length:</label>
<input type="text" id="length" name="length"><br>
<label for="width">Enter Width:</label>
<input type="text" id="width" name="width"><br>
<input type="submit" value="Submit">
</form>
"""
TRIANGLE_FORM = """
<form method="GET">
<h2 class="header3">Triangle Area Calculator</h2>
<label for="base">Enter Base:</label>
<input type="text" id="base" name="base"><br>
<label for="height">Enter Height:</label>
<input type="text" id="height" name="height"><br>
<input type="submit" value="Submit">
</form>
"""
DIAMETER_FORM = """
<form method="GET">
<h2 class="header3">Circle Area Calculator</h2>
<label for="diameter">Enter Diameter:</label>
<input type="text" id="diameter" name="diameter"><br>
<input type="submit" value="Submit">
</form>
"""
RADIUS_FORM = """
<form method="GET">
<label for="radius">Enter Radius:</label>
<input type="text" id="radius" name="radius"><br>
<input type="submit" value="Submit">
</form>
"""
CIRCUMFERENCE_FORM = """
<form method="GET">
<label for="circumference">Enter Circumference:</label>
<input type="text" id="circumference" name="circumference"><br>
<input type="submit" value="Submit">
</form>
"""


def main():
  return process_get_request()

#@app.route('/', methods=["GET"])
#def root_get():
#  return process_get_request()

#@app.route('/', methods=["POST"])
#def root_post():
#  return process_post_request()
def process_get_request():
  request = flask.request
  rectangle_form = process_rectangle(request)
  triangle_form = process_triangle(request)
  circle_diameter_form = process_circle_diameter(request)
  circle_radius_form = process_circle_radius(request)
  circle_circumference_form = process_circle_circumference(request)

  result = flask.render_template('assignment3.html')
  result += rectangle_form + triangle_form
  result += circle_diameter_form + circle_radius_form + circle_circumference_form
  return result


def process_rectangle(request):
  result = RECTANGLE_FORM

  try:
    length = float(request.args["length"])
    width = float(request.args["width"])
    recArea = length * width
    result += "<p> The area of the rectangle is " + str(
        recArea) + ".</p>"

  except:
    result += EMPTY_PARAGRAPH

  #result += EMPTY_PARAGRAPH
  return result

def process_triangle(request):
  result = TRIANGLE_FORM

  try:
    base = float(request.args["base"])
    height = float(request.args["height"])
    tArea = base * height * 0.5
    result += "<p> The area of the triangle is " + str(
        tArea) + ".</p>"

  except:
    result += EMPTY_PARAGRAPH

  #result += EMPTY_PARAGRAPH
  return result

def process_circle_diameter(request):
  request = flask.request
  result = DIAMETER_FORM

  try:
    diameter = float(request.args["diameter"])
    dArea = ((diameter / 2)**2) * 3.14
    result += "<p> The area of the circle is " + str(
        dArea) + ".</p>"

  except:
    result += EMPTY_PARAGRAPH

  #result += EMPTY_PARAGRAPH
  return result


def process_circle_radius(request):
  request = flask.request
  result = RADIUS_FORM

  try:
    radius = float(request.args["radius"])
    rArea = (radius**2) * 3.14
    result += "<p> The area of the circle is " + str(
        rArea) + ".</p>"

  except:
    result += EMPTY_PARAGRAPH

  #result += EMPTY_PARAGRAPH
  return result


def process_circle_circumference(request):
  request = flask.request
  result = CIRCUMFERENCE_FORM

  try:
    circumference = float(request.args["circumference"])
    cArea = ((circumference / 6.28)**2) * 3.14
    result += "<p> The area of the circle is " + str(
        cArea) + ".</p>"

  except:
    result += EMPTY_PARAGRAPH

  #result += EMPTY_PARAGRAPH
  return result


#def process_get_request():
#  request = flask.request
#  result = GET_FORM
#
#  try:
#    fahrenheit = float(request.args["fahrenheit"])
#    celsius = (fahrenheit - 32) * 5 / 9
#    result += "<p>" + str(fahrenheit) + "° Fahrenheit is " + \
#        str(celsius) + "° Celsius</p>"
#  except:
#    result += EMPTY_PARAGRAPH

#  result += POST_FORM + EMPTY_PARAGRAPH + GET_FORM2 + EMPTY_PARAGRAPH
#  return result

#def process_post_request():
#  request = flask.request
#  result = GET_FORM2 + EMPTY_PARAGRAPH + GET_FORM + EMPTY_PARAGRAPH + \
#      POST_FORM
#
#  try:
#    celsius = float(request.form["celsius"])
#    fahrenheit = celsius * 9 / 5 + 32
#    result += "<p>" + str(celsius) + "° Celisus is " + \
#        str(fahrenheit) + "° Fahrenheit</p>"
#  except:
#    result += EMPTY_PARAGRAPH
#
#  return result

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000)
