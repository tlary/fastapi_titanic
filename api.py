from fastapi import FastAPI # import FastAPI class
from pydantic import BaseModel

import numpy as np
import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier

api = FastAPI()

# using Pydantic models to declare request body
# base data as derived from Streamlit Frontend
class titanicData(BaseModel):
	Age: int
	pclassAux: int
	family_size: int
	sex: str
	embarked: str
	
# preprocessed data as returned from API
class modelData(BaseModel):
	Age: int
	child: int
	family_size: int
	Pclass_1: int
	Pclass_2: int
	Pclass_3: int
	Sex_female: int
	Sex_male: int
	Embarked_C: int
	Embarked_Q: int
	Embarked_S: int


# define post method to preprocess data
# using the previously defined Pydantic class as request body
@api.post("/preprocess/", response_model=modelData)
def preprocess_data(data: titanicData):
	
	# child indicator
	child = int(data.Age <= 16)
	
	# passenger class
	Pclass_1=0
	Pclass_2=0
	Pclass_3=0
	if data.pclassAux==1:
	    Pclass_1=1
	if data.pclassAux==2:
	    Pclass_2=1
	if data.pclassAux==3:
	    Pclass_3=1
	    
	# male/female indicators
	Sex_female = 0
	Sex_male = 0
	if data.sex=="female":
	    Sex_female=1
	else:
	    Sex_male=1
	
	# embarked indicators
	Embarked_S = 0
	Embarked_Q = 0
	Embarked_C = 0
	if data.embarked=="Cherbourg":
	    Embarked_C = 1
	if data.embarked=="Queenstown":
	    Embarked_Q = 1
	if data.embarked=="Southampton":
	    Embarked_S = 1
	
	# store preprocessed data / model input as dictionary
	processed = {"Age": data.Age,
                "child": child,
                "family_size": data.family_size,
                "Pclass_1": Pclass_1,
                "Pclass_2": Pclass_2,
                "Pclass_3": Pclass_3,
                "Sex_female": Sex_female,
                "Sex_male": Sex_male,
                "Embarked_C": Embarked_C,
                "Embarked_Q": Embarked_Q,
                "Embarked_S": Embarked_S}
                
        # return preprocessed data
	return processed
	
# define post method to get prediction from model
@api.post("/predict/")
def predict_from_preprocessed(data: modelData):

	# get data from request body
	inputData = data.dict()
	# convert to pd DF since sklearn cannot predict from dict
	inputDF = pd.DataFrame(inputData, index=[0])
	
	# load the Random Forest Classifier
	with open("./rfSimple.pkl", 'rb') as file:
    	    rf = pickle.load(file)
    	# make predictions
	SurvivalProba = rf.predict_proba(inputDF)[0,1]
	survPerc = round(SurvivalProba*100, 1)
	
	return survPerc







