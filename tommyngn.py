from flask import Flask
from flask import render_template
import requests

app=Flask(__name__,template_folder='templates')

@app.route('/')
def home():

    return render_template('index.html')



if __name__== '__main__':
    app.run(host="2601:645:8002:b090:55bf:9b88:983e:cba2",port=5000)

