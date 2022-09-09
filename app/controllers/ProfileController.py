from flask import render_template, request
from app import db
from app.models import NewUser

def profile():
    user = request.args
    username = user.get("username")
    password = user.get("password")
    return render_template("profile.html", username=username, password=password)

def delete():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == None or password == None:
            return "Error, missing parameters."
        
        try: 
            user1 = NewUser.query.filter(NewUser.username==username).first()
            if user1 == None or user1.password != password:
                return "Invalid username or password."
        except Exception as err:
            print("Error while connecting to DB.")
            print(err)
            return "Internal server error."
        try: 
            db.session.delete(user1)
            db.session.commit()
        except Exception as err:
            print("Error while connecting to DB.")
            print(err)
            return "Internal server error."
        
        return render_template("index.html")
    return render_template("delete.html")