from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    ---
    return "<h1 style='text-align: center;'>This is Capstone Project 5 WebApp!</h1>"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True) # specify port=80
