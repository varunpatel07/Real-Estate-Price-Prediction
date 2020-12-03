import json
import numpy as np
import pickle
__location=None
__data_columns=None
__model=None
def get_location_name():
    return __location

def get_price(location,sqft,bhk,bath): 
    try:
        loc_index=__data_columns.index(location.lower())

    except:
        loc_index=-1
    x=np.zeros(len(__data_columns))
    x[0]=sqft
    x[1]=bath
    x[2]=bhk
    if loc_index>=0:
        x[loc_index]=1
    #print(x)
    #print([x])
    return round(__model.predict([x])[0],2)


def load_data():
    print("loading")
    global __data_columns
    global __location

    with open(r"C:\Users\lenovo\Desktop\Real Estate Price Prediction\model\columns.json",'r') as f:
        __data_columns=json.load(f)["data_columns"]
        __location=__data_columns[3:]
    global __model
    with open(r"C:\Users\lenovo\Desktop\Real Estate Price Prediction\model\house_model.pickle",'rb') as f:
        __model=pickle.load(f)
    print("loading done")

if __name__=="util":
    load_data()
    #print(get_location_name()) 
    #print(get_price('1st block jayanagar',1000,3,2))
