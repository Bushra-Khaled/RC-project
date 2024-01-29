import flask 
from flask import render_template, request, redirect, url_for
import json
import uuid
from datetime import datetime
app =flask.Flask("form")


class book():
    def __init__(self, name, phone, email, age, address, appointment, additionalInfo):
        self.name = name
        self.phone = phone
        self.email = email
        self.age = age
        self.address= address
        self.appointment = appointment
        self.additionalInfo =additionalInfo

    @app.route("/add")       
    def create():  #create / update booking function
        #check if the booking data has ID or not.
        get_id = str(request.args.get("id"))
        print(get_id)
        if get_id == '':
            id =  "HUC-"+str(uuid.uuid1().time_low)
        else: 
            id = get_id
        #save the data in an array
        newData = {
            'id' : id ,
            'name' : request.args.get('name'),
            'email' :request.args.get('email'),
            'phone' :request.args.get('phone'),
            'address' :request.args.get('address'),
            'age' :request.args.get('age'),
            'appointment' :request.args.get('appointment'),
            'additionalInfo' :request.args.get('additionalInfo'),
            'entryDate': str(datetime.now().strftime("%d/%m/%Y, at %H:%M"))
        }    
        # update existing booking details 
        with open("booking.json", "r") as file:
            data = json.load(file)
            for i in data:
                if id == i["id"]:
                    with open("booking.json", "w") as file:
                        i.update(newData)
                        json.dump(data, file, indent=4 )
                        msg = i["name"] + "'s booking details had been updated."
                        return render_template("show.html", msg = msg, data = data)
            # create new booking
            else:
                with open("booking.json", "w") as file:
                    data.append(newData)
                    json.dump(data, file, indent=4 )
                    msg = "Dear "+ newData["name"] + ", Your booking had been scheduled on " + newData["appointment"] + "."
                    return render_template("form.html", msg= msg, data=data)  

    @app.route("/dashboard")
    def show(): # fetch the booking file and send the data to the show page
        try:
            with open("booking.json", "r") as file:
                data = json.load(file)
                return render_template("show.html", data = data) 
        except:  
            msg ="NO DATA FOUND"
            return render_template("show.html", msg= msg)  
   
    @app.route("/edit")
    def edit(): # fetch the booking file by id and send its data to the update form 
        with open("booking.json", "r") as file:
            data = json.load(file)
            id = str(request.args.get("id"))            
            if id == '':
                return render_template("form.html", data= [])
            else: 
                for i in data:
                    if i["id"] == id :
                        patientData = i
                        return render_template("form.html", data = patientData, id = id) 

    @app.route("/delete")
    def delete(): # fetch the booking file by id and delete its related booking data
        with open("booking.json", "r") as file:
            data = json.load(file)
            id = request.args.get("id")
            for i in data:
                if id == i["id"]:
                    msg = i["name"] + "'s appointment on " + i["appointment"] + " had been cancelled "
                    data.remove(i)               
            with open("booking.json", "w") as file:
                json.dump(data, file, indent=4 )
                return render_template("show.html", data = data, msg = msg)  


@app.route("/auth")
def authUser(): # check if the user is exist in the database
    userName =  request.args.get("userName")
    password = request.args.get("password")
    with open("users.json", "r") as file:
        users = json.load(file)
        for i in users:
            if userName == i["userName"]: 
                if password == i["password"]:
                    return redirect(url_for("show"))
        else:
            msg = "User name or password is not correct! Please try again!"
            return render_template("login.html", msg =msg)

@app.route("/signup")
def newUser(): # check if it's existing before, and if not, will add new user to the database.
    userName =  request.args.get("userName")
    password = request.args.get("password")
    newUser = { 
        "userName": userName,
        "password": password
    }
    with open("users.json", "r") as file:
        users = json.load(file)
        for i in users:
            if userName == i["userName"]: 
                if password == i["password"]:
                    msg = "This user had registered before!"
                    return render_template("login.html", msg =msg) 
        else:
            users.append(newUser)
            with open("users.json", "w") as file:
                json.dump(users, file, indent=4 )
                msg = "User added successfuly, login and explore more!!"
            return render_template("login.html", msg =msg) 

@app.route("/booking")
def bookingPage():
    return render_template("form.html")

@app.route("/")
def loginPage():
    return render_template("login.html")


