#Script that imports the Random Forest Model
# and creates a webservice
import pandas as pd 
import pickle
import numpy as np
from sklearn.model_selection import GridSearchCV
from flask import Flask,request

#Import the module
model_file = open("epi.pk","rb") 
est = pickle.load(model_file)
model_file.close()

#Create the app
app = Flask(__name__)
@app.route('/epi', methods=['POST'])
#This is a pretty simple way of getting the request and then
#casting it into a array
#The app can be improved by incorporating error handling
def epi():
      eegdata=map(int, request.form["eeg"].split(','))
      print eegdata
      data=np.array([eegdata]).reshape(-1,178)
      y=est.predict(data)[0]
      y_prob=est.predict_proba(data)[0][y-1]
      res="Error in Prediction"
      if(y==1):
       res="Eplipetic with probabilty " + str(y_prob)
      if(y==2):
       res="Non Eplipetic with probabilty " + str(y_prob)
      return res
     
