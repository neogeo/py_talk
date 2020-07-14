import requests


from flask import Flask
app = Flask(__name__)

def io_call():
    res = requests.get('https://k7hf6ipvq8.execute-api.us-west-2.amazonaws.com/sleep_lambda')
    res.raise_for_status()

    print('io finished')
    return res.json()

@app.route('/sync')
def sync():

    io_call()
    io_call()
    res = io_call()
    
    return res 
