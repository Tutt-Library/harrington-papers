__author__ = "Jeremy Nelson"

from flask import Flask

app = Flask(__name__)

from views import *

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)
