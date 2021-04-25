"""
Chris Cortes' Flask API.
"""

from flask import Flask, render_template, send_from_directory, abort


app = Flask(__name__)

# this is the defult webpage
@app.route("/")
def hello():
    return "UOCIS docker demo!\n"

# reads the path entered
@app.route("/<path:path>")
def read_path(path):
    # checks if path contains forbidden characters, results in error 403 if found
    if "~" in path or ".." in path or "//" in path:
        abort(403)
    else:
        # trys to open file 
        try:
            return send_from_directory('pages',path)
        # will result in error 404 if no file found
        except:
            abort(404)

# error 403, takes the error html from templates and displays it
@app.errorhandler(403)
def forbidden_403(e):
    return render_template('403.html'), 403

# error 404, takes the error html from templates and displays it
@app.errorhandler(404)
def not_found_404(e):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
