from flask import Flask, request, jsonify, render_template, blueprints, Blueprint
import json
import os
import datetime





from myblueprints.Cars_bpV1 import Cars_bpV1



app = Flask(__name__)



app.register_blueprint(Cars_bpV1, url_prefix='/api/v1') 

 
 
#http://127.0.0.1:5000/api/v1

#http://127.0.0.1:5000/api/v1/Car_Inventory
#http://127.0.0.1:5000/api/v1/Add_New_Car_Data
#http://127.0.0.1:5000/api/v1/Car_Remove
#http://127.0.0.1:5000/api/v1/Change_Car_Information

#http://127.0.0.1:5000/api/v1/json



# Startar applikationen
if __name__ == "__main__": 
    # debug=True gör att servern startar om automatiskt när du ändrar i koden
    app.run(debug=True)