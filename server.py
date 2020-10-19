
import os
import requests
from flask import Flask


app = Flask(__name__)

@app.route("/")
def hello():
    
    url = os.environ.get('url','127.0.0.1')
    
    try:
        r = requests.get('http://{}'.format(url))
        text=r.text
    except Exception as e:
        text='----------'
 
    return "url: {url}  {text}".format(url=url, text=text)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
