from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World! Esta es una prueba"

if __name__ == "__main__":
    application.run()
