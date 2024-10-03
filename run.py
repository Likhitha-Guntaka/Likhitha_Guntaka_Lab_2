from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/time')
def get_time():
    return str(datetime.now())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
