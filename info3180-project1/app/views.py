
from app import app
import os
from flask import session,flash,render_template, request, redirect, url_for

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')






@app.route('/profile',methods=['POST','GET'])
def profile():
    if request.method=="POST":
        if request.form['fname']=="":
            error="please enter first name"
        elif request.form['lname']=="":
            error="enter last name"

    return  render_template('create_profile.html',error='error')






@app.route('/profiles',methods=["GET"])
def profiles():
   return render_template('view_profile.html')







app.route('profile/<userid>',methods=["POST"])
def profile():
    return render_template('view_profile_list')








if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8888")
