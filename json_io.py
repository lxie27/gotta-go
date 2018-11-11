from flask import Flask
app = Flask(__name__)

@app.route("/output")
def output():
    return "Hello world!"

if __name__ == "__main__":
    app.run()

