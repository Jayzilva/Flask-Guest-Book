from flask import Flask


app = Flask(__name__)  #instantiate Flask application & passing the module name
    
    #creating a route
@app.route('/') #passing the endpoint as  paramenter
def index(): #view funtion under the decorater
    return "<h1>Hello World</h1>"
    
if __name__ == "__main__": #if call directly from the CMD
    app.run(debug=True)
    