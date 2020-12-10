import pandas as pd
import flask
from flask import request
#import json
#import requests
import pickle
import dashboard
from  warnings import simplefilter
from sklearn.exceptions import ConvergenceWarning
simplefilter("ignore", category=ConvergenceWarning)

# Use pickle to load in the pre-trained model.
with open(r"model/model_bit.pkl", 'rb') as f:
    model = pickle.load(f)
f.close()

server = flask.Flask(__name__)
app = dashboard.get_dash(server)

@app.server.route("/", methods=["GET"])
def index():
    return flask.render_template("main.html")

@app.server.route('/twin', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        print("we are in get now")
        torque = request.args.get('torque', type=int)
        print(torque)
        temperature = request.args.get('temperature', type=int)
        print(temperature)
        weight_on_bit = request.args.get('weight_on_bit', type=int)
        print(weight_on_bit)
        apiinput_variables = pd.DataFrame([[torque, temperature, weight_on_bit]],
                                       columns=['torque', 'temperature', 'weight_on_bit'],
                                       dtype=float)
    
        prediction = model.predict(apiinput_variables)
    
        prediction = int(prediction[0])
        
        return {
            "prediction": prediction,
        }
            
        
    if flask.request.method == 'POST':    
        print("we are in post now")
        torque = request.form.get('torque', type=int)
        print(torque)
        temperature = request.form.get('temperature', type=int)
        print(temperature)
        weight_on_bit = request.form.get('weight_on_bit', type=int)
        print(weight_on_bit)
        
        apiinput_variables = pd.DataFrame([[torque, temperature, weight_on_bit]],
                                       columns=['torque', 'temperature', 'weight_on_bit'],
                                       dtype=float)
    
        prediction = model.predict(apiinput_variables)
    
        prediction = int(prediction[0])

        return {
                "prediction": prediction,
            }
        
        
if __name__ == '__main__':
    app.run_server(port=5001, debug=False)
        
