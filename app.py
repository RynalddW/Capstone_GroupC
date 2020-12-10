import pandas as pd
import flask
from flask import request 
import requests
import pickle
import dashboard
from  warnings import simplefilter
from sklearn.exceptions import ConvergenceWarning
simplefilter("ignore", category=ConvergenceWarning)

# Use pickle to load in the pre-trained model.

with open(r"model/model_bit.pkl", 'rb') as f:
    models = pickle.load(f)
f.close()


server = flask.Flask(__name__)
app = dashboard.get_dash(server)


@app.server.route("/", methods=["GET"])
def index():
    return flask.render_template("main.html")

@app.server.route('/drill', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return(flask.render_template('main.html'))
    if flask.request.method == 'POST':
        # temperature = flask.request.form['temperature']
        torque = flask.request.form['torque']
        temperature = flask.request.form['temperature']
        weight_on_bit = flask.request.form['weight_on_bit']
        
        input_variables = pd.DataFrame([[torque, temperature, weight_on_bit]],
                                       columns=['torque', 'temperature', 'weight_on_bit'],
                                       dtype=float)
        print(input_variables)
        prediction = models.predict(input_variables)
        return flask.render_template('main.html', original_input={'torque': torque, 'Temperature':temperature, 'weight_on_bit':weight_on_bit},
                                     result=prediction)
        
        #return {"result" : prediction}
        
@app.server.route('/modelo', methods=['GET', 'POST'])
def model():
    if flask.request.method == 'GET':
        return(flask.render_template('model.html'))
    
        
    
@app.server.route('/api', methods=['GET', 'POST'])
def values():
#    if flask.request.method == 'GET':
#        return(flask.render_template('main.html'))
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
        
               
#        
#        temp_value =  1234 #random.uniform(1,10000)
#        torque_value =  23 #random.uniform(1, 47)
#        weight_on_bit_value = 34 #random.uniform(0, 40)
#        
#        
#       
        url = ("https://capstonegrpctwin.herokuapp.com/twin?" + "torque=" + str(torque) + "&temperature=" + str(temperature) +"&weight_on_bit=" + str(weight_on_bit))
        
        print(url)
#        

        r = requests.get(url).json()
        r = (r["prediction"])
        print(r)

        return flask.render_template('index.html', result=r)
        
if __name__ == '__main__':
    app.run_server(port=5000, debug=False)