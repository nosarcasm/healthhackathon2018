from medtracker import *

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/assets/<path:path>')
def send_js(path):
    return send_from_directory('/app/assets', path)
