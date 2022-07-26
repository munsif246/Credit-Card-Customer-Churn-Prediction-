import numpy as np
from flask import Flask, request, jsonify, render_template,redirect, url_for
import pickle

app = Flask(__name__) #initializing the flask we have to do it
model = pickle.load(open('Random_Forest.pkl', 'rb')) #always create(not load) a using jupyter notebook not using spyder

@app.route('/')
def home():
    return render_template('index.html') #routing our html file which is in templates folder

@app.route('/service')
def service():
    return render_template('model.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/predict',methods=['GET','POST']) #if we run http://127.0.0.1:5000/predict this code under this will be executed
def predict():
    
    if request.method == 'POST':
        int_features = [float(x) for x in request.form.values()]#input values
        final_features = [np.array(int_features)] #coverting it to array 
        prediction = model.predict(final_features) #predicting
        
        x=""
        if(prediction==0):
            x="Churn"
        else:
            x="not Churn"
        return render_template('model.html', prediction_text='The Customer will {}'.format(x))
   
    #output = round(prediction[0], 2)# rounding off the output to 2nd decimal

    

##these things are for request.py


if __name__ == "__main__":
    app.run(debug=True)
    
