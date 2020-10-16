
import os
from flask import Flask


app = Flask(__name__)

@app.route("/")
def hello():
    
    ip = os.environ.get('ip','没有找到ip地址')
    
    return "ip: {}".format(ip)


if __name__ == "__main__":
    app.run()
