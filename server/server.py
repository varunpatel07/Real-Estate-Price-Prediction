from flask import Flask,request,jsonify
import util
from flask_cors import CORS,cross_origin

app=Flask(__name__)
CORS(app)

@app.route("/get_location_names")
def get_location_names():
    response=jsonify({
        "locations":util.get_location_name()
    })

    return response

@app.route("/predict_price",methods=["GET","POST"])

def predict_price():
    #print(request.is_json)
    content=request.get_json()
    #print(type(content))
    total_sqft=float(content["sqft"])
    location=content["city"]
    bhk=int(content["bhk"])
    bath=int(content["bath"])
     
    response= jsonify({
         "price":util.get_price(location,total_sqft,bhk,bath)
     })

    response.headers.add("Access-Control-Allow-Origin","*")
    return response



if __name__=="__main__":
    print("starting server")
    app.debug = True
    app.run()
    
