from flask import Blueprint, jsonify, render_template, request
import requests
import datetime
import json


Cars_bpV1 = Blueprint('Cars_bpV1', __name__)



##################################################################
@Cars_bpV1.route('/', methods=['GET'])
def index():
    return "Hello start page"



##################################################################
@Cars_bpV1.route('/Add_New_Car_Data', methods=['POST'])
def Add_New_Car_Data():
    with open('cars.json', 'r', encoding="UTF-8") as file_car_pointer:
        Add_New_Car_Data = json.load(file_car_pointer)
        
    New_Car_Regnr = request.form.get('Regnr')
    New_Car_Make = request.form.get('Make')
    New_Car_Model = request.form.get('Model')
    New_Car_Year = request.form.get('Year')
    New_car_Color = request.form.get('Color')
    New_Car_Owner_Firstname = request.form.get('FirstName')
    New_Car_Owner_Lastname = request.form.get('LastName')
    New_Car_Status = request.form.get('status')
    New_Car_Added_Time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return 200



##################################################################
@Cars_bpV1.route('/Car_Inventory', methods=['GET'])
def Car_Inventory():
    with open('cars.json', 'r', encoding="UTF-8") as file_car_pointer:
        Car_Data = json.load(file_car_pointer)
        return Car_Data



##################################################################
@Cars_bpV1.route('/Car_Remove', methods=['DELETE'])
def Car_Remove():   
    with open('cars.json', 'r', encoding="UTF-8") as file_car_pointer:
        Car_Data = json.load(file_car_pointer)
    if regnr in Car_Data.keys():
        del Car_Data[regnr]
        with open('cars.json', 'w', encoding="UTF-8") as file_car_pointer:
            json.dump(Car_Data, file_car_pointer, indent=4)
        return 200
    
    
    
    
##################################################################
@Cars_bpV1.route('/Change_Car_Information', methods=['PUT'])
def Change_Car_Information():
    with open('cars.json', 'r', encoding="UTF-8") as file_car_pointer:
        Car_Data = json.load(file_car_pointer)
    New_Car_Regnr = request.form.get('Regnr')
    New_Car_Make = request.form.get('Make')
    New_Car_Model = request.form.get('Model')
    New_Car_Year = request.form.get('Year')
    New_car_Color = request.form.get('Color')
    New_Car_Owner_Firstname = request.form.get('FirstName')
    New_Car_Owner_Lastname = request.form.get('LastName')
    New_Car_Status = request.form.get('status')
    New_Car_Added_Time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    for key in Car_Data.keys():
        if key == New_Car_Regnr:
            Car_Data[key]['Make'] = New_Car_Make
            Car_Data[key]['Model'] = New_Car_Model
            Car_Data[key]['Year'] = New_Car_Year
            Car_Data[key]['Color'] = New_car_Color
            Car_Data[key]['Owner_Firstname'] = New_Car_Owner_Firstname
            Car_Data[key]['Owner_Lastname'] = New_Car_Owner_Lastname
            Car_Data[key]['Status'] = New_Car_Status
            Car_Data[key]['Added_Time'] = New_Car_Added_Time

    with open('cars.json', 'w', encoding="UTF-8") as file_car_pointer:
        json.dump(Car_Data, file_car_pointer, indent=4)
    return 200



    
    


##################################################################
@Cars_bpV1.route('/json', methods=['GET', 'POST', 'DELETE', 'PUT'])
def Load_Json():
    with open('cars.json', 'r', encoding="UTF-8") as file_car_pointer:
        Car_Data = json.load(file_car_pointer)

def Save_Json():
    with open('cars.json', 'w', encoding="UTF-8") as file_car_pointer:
        json.dump(Car_Data, file_car_pointer, indent=4) 
        
        
