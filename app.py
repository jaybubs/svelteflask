from flask import Flask, send_from_directory
import random

app = Flask(__name__)

# main page
@app.route("/")
def hi():
    return send_from_directory("dist", "index.html")

# static
@app.route("/<path:path>")
def home(path):
    return send_from_directory("dist", path)

@app.route("/rand")
def rand():
    return str(random.randint(0,100))

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5175,debug=True)
