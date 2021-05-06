from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<name>')
def hi(name):
    print(name)
    return "Hi " + name

@app.route('/repeat/<num>/<name>')
def repeat(name, num):
    return int(num) * name

if __name__=="__main__":  
    app.run(debug=True)