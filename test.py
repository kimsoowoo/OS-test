from flask import Flask

application = Flask(__name__)

@application.route("/")
def home():

    return "<B> Hello. This is a test. </B>"

if __name__ == "__main__":
    application.run(debug=True)
