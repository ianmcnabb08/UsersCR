from flask import Flask, render_template, request, redirect
# import the class from friend.py
from user import User
app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/user')

@app.route('/user')
def users():
    return render_template("read.html", user=User.get_all())

@app.route('/user/new')
def new():
    return render_template("create.html")

@app.route('/user/create', methods=["POST"])
def create_user():
    print(request.form)
    User.save(request.form)
    return redirect('/user/new')
            
if __name__ == "__main__":
    app.run(debug=True)