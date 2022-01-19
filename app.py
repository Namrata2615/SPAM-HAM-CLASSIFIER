from flask import Flask,render_template,request,jsonify
import pandas as pd
import numpy as np 
import joblib
import logging
from config import config

logging.basicConfig(filename=config.logfile_path,level=logging.DEBUG)

app = Flask(__name__)


model = joblib.load(config.model_path)

@app.route('/',methods=['GET', 'POST'])
def index():
    try:
        if request.method == 'POST':
            message = request.form.get('message')
            logging.info("Message Received")
            output = model.predict([message])
            if output == [0]:
                result = "This Message is Not a SPAM Message."
            else:
                result = "This Message is a SPAM Message." 
            return render_template('index.html', result=result,message=message)      

        else:
            logging.warning("POST Method not used for the request")
            return render_template('index.html')  
    except Exception as e:
        logging.error(str(e))
        return render_template('index.html') 

if __name__ == '__main__':
    app.run(debug=True)