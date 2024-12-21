from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")

def index():
  #name = request.args["name"] #creating variable titled "name", setting it to request....
  name = request.args.get("name", "world")
    #.get is a function that comes with a dictionary
    # if you didn't specify "world" as the fallback, would default to None
  return render_template("index.html", placeholder=name) 
#(Creates?) argument (i.e., named parameter) titled "placeholder," value of this argument set to name
# So recall that Python supports named parameters, which just means that you can pass in multiple arguments to a function. But you can specify them by name. So I am calling one of these arguments placeholder. And I'm setting the value of that argument equal to name, which itself is a variable that I defined just a moment ago. 

