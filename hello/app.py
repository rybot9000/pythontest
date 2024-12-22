from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")

def index():
  #name = request.args["name"] #creating variable titled "name", setting it to request....
  name = request.form.get("name", "world")
    #.get is a function that comes with a dictionary
    # if you didn't specify "world" as the fallback, would default to None
    #request.args is for get, request.forms is for post
  return render_template("index.html") 
  #return render_template("index.html", name=name) 
#(Creates?) argument (i.e., named parameter) titled "placeholder," value of this argument set to name
# So recall that Python supports named parameters, which just means that you can pass in multiple arguments to a function. But you can specify them by name. So I am calling one of these arguments placeholder. And I'm setting the value of that argument equal to name, which itself is a variable that I defined just a moment ago. 
#to the left of the equal sign (e.g., placeholder) is the name of the parameter, and to the left
#of the equal sign is the value of the parameter. Prof. says in flask world often see stuff like
#name=name, which isn't super bad, maybe helpful to equal self


    
@app.route("/greet", methods=["POST"])

def greet():
  name = request.args.get("name","world")
  return render_template("greet.html", name=name) 
 
