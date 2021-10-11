from flask import request, Blueprint
import requests
import schedule
import time


data = Blueprint('data', __name__)


@data.route('/get')
def get_data():
    return requests.get("http://localhost:3030/api/test").content

def fetch():
    print(requests.get("http://localhost:3030/api/test").content)

schedule.every().sunday.do(fetch)

while True:

    schedule.run_pending()
    time.sleep(1)