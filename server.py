
import os
from flask import Flask


app = Flask(__name__)

@app.route("/")
def hello():
    
    ip = os.environ.get('ip','127.0.0.1')
    
    return "ip: {}".format(ip)


if __name__ == "__main__":
    app.run()
