from flask import Flask


app = Flask(__name__)  #instantiate Flask application & passing the module name
    
    #creating a route
@app.route('/') #passing the endpoint as  paramenter
def index(): #view funtion under the decorater
    return "<h1>Hello World</h1>"

@app.route("/home")
def home():
    return "<h2>The Home Page</h2>"
    
@app.route("/place/<place>")
def location(place):
    return "<h2>You are on the" + place +"Page</h2>"

if __name__ == "__main__": #if call directly from the CMD
    app.run(debug=True)
    