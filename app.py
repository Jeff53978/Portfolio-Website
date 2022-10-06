import flask

app = flask.Flask(__name__)

@app.get("/")
def main():
    return flask.render_template("home.html")

app.run(debug=True, host="0.0.0.0", port=4002)