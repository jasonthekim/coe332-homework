import redis
from flask import Flask, request
import json


app = Flask(__name__)


@app.route('/data', methods = ['POST', 'GET'])
def read_data():
    """
    This route loads the ML_Data_Sample into our Redis database instance through the POST request, and reads the dataset out of Redis, returning it as a JSON list, through the GET request.

    Returns:
    List of dicts (list): Info on meteorite landings data
    """
    rd = redis.Redis(host='172.17.0.18', port=6379)
    
    if request.method == 'POST':
        with open('ML_Data_Sample.json', 'r') as f:
            ml_data = json.load(f)
        
        for item in ml_data['meteorite_landings']:
            rd.set(item['id'], json.dumps(item))
        return f'Data has been read from file\n'    

    ml_list = []
    if request.method == 'GET':
        for i in range(10001, 10301, 1):
            ml_list.append(json.loads(rd.get(i)))
        return json.dumps(ml_list, indent=2)

