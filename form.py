import flask 
from flask import render_template, request, redirect, url_for
import json
import uuid
from datetime import datetime
app =flask.Flask("form")

class book:
    def __init__(self, name, phone, email, age, address, appointment, additionalInfo):
        self.name = name
        self.phone = phone
        self.email = email
        self.age = age
        self.address= address
        self.appointment = appointment
        self.additionalInfo =additionalInfo

    @app.route("/add")       
    def create():
        get_id = request.args.get("id")
        if get_id == None:
            id =  "HUC-"+str(uuid.uuid1().time_low)
        else: 
            id = get_id
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
        with open("booking.json", "r") as file:
            data = json.load(file)
            for i in data:
                if id == i["id"]:
                    with open("booking.json", "w") as file:
                        i.update(newData)
                        json.dump(data, file, indent=4 )
                        msg = i["name"] + "'s booking details had been updated."
                        return render_template("show.html", msg = msg, data = data)
            else:
                with open("booking.json", "w") as file:
                    data.append(newData)
                    json.dump(data, file, indent=4 )
                    msg = "Dear "+ newData["name"] + ", Your booking had been scheduled on " + newData["appointment"] + "."
                    return render_template("form.html", msg= msg)  

    @app.route("/show")
    def show():
        try:
            with open("booking.json", "r") as file:
                data = json.load(file)
                return render_template("show.html", data = data) 
        except:  
            msg ="no data found"
            return render_template("show.html", msg= msg)  
   
    @app.route("/edit")
    def edit():
        with open("booking.json", "r") as file:
            data = json.load(file)
            id = str(request.args.get("id"))
            for i in data:
                if i["id"] == id :
                    patientData = i
                    return render_template("edit.html", data = patientData, id = id)  

    @app.route("/delete")
    def delete():
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
def authUser():
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
def newUser():
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
                msg = "User added successfuly"
            return render_template("show.html", msg =msg) 

@app.route("/booking")
def bookingPage():
    return render_template("form.html")

@app.route("/")
def loginPage():
    return render_template("login.html")


