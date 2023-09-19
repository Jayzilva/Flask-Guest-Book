from flask import Flask, render_template


app = Flask(__name__)  #instantiate Flask application & passing the module name
    
    #creating a route
@app.route('/') #passing the endpoint as  paramenter
def index(): #view funtion under the decorater
    return "<h1>Hello World</h1>"

@app.route("/home", methods=["GET" , "POST"])
def home():
    links = ["https://www.youtube.com/" , "https://www.canva.com/" , "http://127.0.0.1:5000/" , "https://github.com/"]
    
    return render_template("index.html", myvar="Var x" ,links=links) #render_templates look at the templates file


if __name__ == "__main__": #if call directly from the CMD
    app.run(debug=True)
    