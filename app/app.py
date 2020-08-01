"""
https://github.com/behajakum/python-github-cicd
sample flask hello world to demonstrate cicd with github actions
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello, World!</h1>"

if __name__ == "__main__":
    app.run()
