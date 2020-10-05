from flask import Flask,request,jsonify
import util
app=Flask(__name__)

@app.route("/get_location_names")
def get_location_names():
    response=jsonify({
        "locations":util.get_location_name()
    })
    response.headers.add("Access-Control-Allow-Origin","*")
    return response

@app.route("/predict_price",methods=["POST"])
def predict_price():
    total_sqft=float(request.form["total_sqft"])
    location=request.form["location"]
    bhk=int(request.form["bhk"])
    bath=int(request.form["bath"])
     
    response= jsonify({
         "price":util.get_price(location,total_sqft,bhk,bath)
     })

    response.headers.add("Access-Control-Allow-Origin","*")
    return response



if __name__=="__main__":
    print("starting server")
    app.debug = True
    app.run()
    #print(get_location_names())
