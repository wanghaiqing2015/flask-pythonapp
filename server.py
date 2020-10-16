
import os
import requests
from flask import Flask


app = Flask(__name__)

@app.route("/")
def hello():
    
    ip = os.environ.get('ip','127.0.0.1')
    
    try:
        r = requests.get('http://{}'.format(ip))
        text=r.text
    except Exception as e:
        text='----------'
 
    return "ip: {ip}  {text}".format(ip=ip, text=text)


if __name__ == "__main__":
    app.run()
