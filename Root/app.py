# Demonstrates a complete server-side website using:
#   * static HTML and CSS
#   * a template
#   * a code module
#
# NOTE: Static pages (html, css, images, etc.) must be placed in
# a folder named "static". Template pages must be placed in a folder
# named "templates".
#
# Folder structure:
# app.py
# hello.py
# static
#   index.html
#   static.html
#   styles.css
# templates
#   template.html
#
# References:
#   https://en.wikiversity.org/wiki/Flask/Hello_World
#   https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

import flask
import lesson1
import lesson2

app = flask.Flask(__name__)

@app.route("/")
def show_root():
    return route_path("index.html")

@app.route("/<path:path>")
def route_path(path):
#    if path == "code":
#        return hello.main()
#    elif path == "template":
#        data = {
#            "greeting": "Hello",
#            "name": "world"
#        }
#        return flask.render_template('template.html', data=data)
#    else:
#        # Process any unrecognized route as a static file request
#        return flask.send_from_directory(app.static_folder, path)  
    if path == "lesson1":
        return lesson1.main()
    elif path == "lesson2":
        #return lesson2.main()
        return lesson2.main()
    
#    elif path == "lesson3":
#    elif path == "lesson4":   
#    elif path == "lesson5": 
#    elif path == "lesson6": 
#    elif path == "lesson7": 
#    elif path == "lesson7":  
#    elif path == "lesson8": 
#    elif path == "lesson9": 
#    elif path == "lesson10": 
#    elif path == "lesson11": 
#    elif path == "lesson12":
    
    else:
        # Process any unrecognized route as a static file request
        return flask.send_from_directory(app.static_folder, path)    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)