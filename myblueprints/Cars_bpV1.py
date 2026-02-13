from flask import Blueprint, jsonify, render_template, request
import requests
import datetime
import json


Cars_bpV1 = Blueprint('Cars_bpV1', __name__)



##################################################################
@Cars_bpV1.route('/', methods=['GET'])
def index():
    return render_template('index.html')


##################################################################
@Cars_bpV1.route('/Add_New_Car_Data', methods=['POST', 'GET'])
def Add_New_Car_Data():
    status = request.form.get('status')

    with open('cars.json', 'r', encoding="UTF-8") as file_car_pointer:
        Add_New_Car_Data = json.load(file_car_pointer)
    
    if status == 'Uthämtad':
        json.pop.Add_New_Car_Data["Regnr"]
    
    
    New_Car_Regnr = request.form.get('Regnr')
    New_Car_Make = request.form.get('Make')
    New_Car_Model = request.form.get('Model')
    New_Car_Year = request.form.get('Year')
    New_car_Color = request.form.get('Color')
    New_Car_Owner_Firstname = request.form.get('FirstName')
    New_Car_Owner_Lastname = request.form.get('LastName')
    New_Car_Status = request.form.get('status')
    New_Car_Added_Time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    Add_New_Car_Data[New_Car_Regnr] = {
        "Regnr": New_Car_Regnr,
        "Make": New_Car_Make,
        "Model": New_Car_Model,
        "Year": New_Car_Year,
        "Color": New_car_Color,
        "Owner_Firstname": New_Car_Owner_Firstname,
        "Owner_Lastname": New_Car_Owner_Lastname,
        "Status": New_Car_Status,
        "Added_Time": New_Car_Added_Time}
    
    with open('cars.json', 'w', encoding="UTF-8") as file_car_pointer:
        json.dump(Add_New_Car_Data, file_car_pointer, indent=4)
    return render_template('index.html', action="add"), 200



##################################################################
@Cars_bpV1.route('/Car_Inventory', methods=['POST', 'GET'])
def Car_Inventory():
    with open('cars.json', 'r', encoding="UTF-8") as file_car_pointer:
        Car_Data = json.load(file_car_pointer)

    if request.form.get('DisplayAll'):
        return jsonify(Car_Data), 200

    for key in Car_Data.keys():
        if key == request.form.get('Regnr'):
            return jsonify(Car_Data[key]), 200
    
    if "Regnr" not in Car_Data.keys():
        return render_template('index.html', error="True", action='check'), 404





##################################################################
@Cars_bpV1.route('/Car_Remove', methods=['POST', 'GET'])
def Car_Remove():   
    Car_Data = []
    with open('cars.json', 'r', encoding="UTF-8") as file_car_pointer:
        Car_Data = json.load(file_car_pointer)
    if "Regnr" in Car_Data.keys():
        del Car_Data["Regnr"]
        with open('cars.json', 'w', encoding="UTF-8") as file_car_pointer:
            json.dump(Car_Data, file_car_pointer, indent=4, ensure_ascii=False, encoding="UTF-8")
            
    return 'allt gick bra!', 200
    
    
  
    
##################################################################
@Cars_bpV1.route('/Change_Car_Information', methods=['POST', 'GET'])
def Change_Car_Information():
    with open('cars.json', 'r', encoding="UTF-8") as file_car_pointer:
        Car_Data = json.load(file_car_pointer)
        
    regnr = request.form.get('Regnr')
    fulloptions = request.form.get('fulloptions')
    
    if regnr not in Car_Data.keys():
        return render_template('index.html', error="True", action='update'), 404

    if regnr in Car_Data.keys() and fulloptions != "True":
        return render_template('index.html', fulloptions = "True", action='update'), 200
    
    if fulloptions == "True" and regnr in Car_Data.keys():
        
        if request.form.get('Make') != "":
            Car_Data[regnr]['Make'] = request.form.get('Make')
        if request.form.get('Model') != "":
            Car_Data[regnr]['Model'] = request.form.get('Model')
        if request.form.get('Year') != "":
            Car_Data[regnr]['Year'] = request.form.get('Year')
        if request.form.get('Color') != "":
            Car_Data[regnr]['Color'] = request.form.get('Color')
        if request.form.get('FirstName') != "":
            Car_Data[regnr]['Owner_Firstname'] = request.form.get('FirstName')
        if request.form.get('LastName') != "":
            Car_Data[regnr]['Owner_Lastname'] = request.form.get('LastName')
        
        Car_Data[regnr]['Status'] = request.form.get('status')
        
        with open('cars.json', 'w', encoding="UTF-8") as file_car_pointer:
            json.dump(Car_Data, file_car_pointer, indent=4)
            
        return render_template('index.html', Carstatus='updated', action='update', error='False'), 200
    

         
    

""" 
##################################################################
@Cars_bpV1.route('/Change_Car_Information', methods=['POST', 'GET'])
def Change_Car_Information():
    with open('cars.json', 'r', encoding="UTF-8") as file_car_pointer:
        Car_Data = json.load(file_car_pointer)
    regnr = request.form.get('Regnr')
    
    if regnr not in Car_Data.keys():
        return render_template('index.html', error="True", action='update'), 404
    
    if regnr in Car_Data.keys():
        
        return render_template('index.html',action='update', error='False'), 200
    
 """
    


##################################################################
@Cars_bpV1.route('/json', methods=['GET', 'POST', 'DELETE', 'PUT'])
def Load_Json():
    Car_Data = []
    with open('cars.json', 'r', encoding="UTF-8") as file_car_pointer:
        Car_Data = json.load(file_car_pointer)

def Save_Json():
    Car_Data = []
    with open('cars.json', 'w', encoding="UTF-8") as file_car_pointer:
        json.dump(Car_Data, file_car_pointer, indent=4) 
        
        
##################################################################
@Cars_bpV1.route('/Carchoice', methods=['POST'])
def Carchoice():
    action = request.form.get('action')
    
    if action == "add":
        return render_template('index.html', action=action)
    elif action == "update":
        return render_template('index.html', action=action)
    elif action == "check":
        return render_template('index.html', action=action)
    elif action == "delete":
        return render_template('index.html', action=action)
    
    elif action == "CheckRegnr":
        return render_template('index.html', action=action, error="False")
