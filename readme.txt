Start app.py  locally, it runs on port 5000

twin.py is deployed on Heroku cloud -  alternatively you can spin it up locally it will run on port 5001 (twin)
It can be reached wit a URL constructed like this:  https://capstonegrpctwin.herokuapp.com/twin?torque=4&temperature=8423&weight_on_bit=48   and replies with JSON output 

test API call with CURL:
curl -X POST -H "Content-Type: application/x-www-form-urlencoded" -i "http://127.0.0.1:5001/twin" --data "torque=1234&temperature=23&weight_on_bit=34"
curl -X POST -H "Content-Type: application/x-www-form-urlencoded" -i "http://127.0.0.1:5000/api" --data "torque=1234&temperature=23&weight_on_bit=34"

Alternatively test with RESTclient or similar browser plugin 
