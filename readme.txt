git clone https://github.com/wanghaiqing2015/flask-pythonapp
cd flask-pythonapp/
pip3 install -r requirements.txt
pyinstaller  --clean server.py   --additional-hooks-dir=.

docker build -t frontend   .
docker run -it -p 5000:5000 frontend

docker save -o frontend.tar frontend