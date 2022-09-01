from flask import Flask 
app = Flask(__name__)

@app.route("/")
def hello():
    return "Halo Rosy"

if __name__ == "__main__":
    app.run()