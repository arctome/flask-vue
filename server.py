# export FLASK_APP=server.py
from flask import Flask
from flask import Response
from flask import request
import simplejson as json

app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/api/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            errResp = Response(json.dumps({"code": -1, "msg": "file not found"}))
            errResp.headers['Access-Control-Allow-Origin'] = '*'
            errResp.headers['Content-Type'] = 'application/json'
            return errResp
        file = request.files['file']
        blob = file.read()
        size = len(blob)
        resp = Response(json.dumps({"code": 0, "size": size}))
        resp.headers['Access-Control-Allow-Origin'] = '*'
        resp.headers['Content-Type'] = 'application/json'
        return resp

if __name__ == "__main__":               # on running python app.py
    app.run(host="127.0.0.1",port = 5000)   # run the flask app  