from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string("<body style='background-color: #9dffff; height=100%; display:flex;'><div style='font-family: Poppins; display:flex; flex-direction: column; align-self: center; width: 100%'><h1 style='text-align:center'>Welcome to Jenkins CI/CD Pipeline for Python Application</h1><h2 style='text-align:center'>Also with SAST Security Scan</h2></div></body>")
