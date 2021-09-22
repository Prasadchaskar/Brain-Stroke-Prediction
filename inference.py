import pickle
import numpy as np
import pandas as pd
model = pickle.load(open('stroke.pkl', 'rb'))
scaler = pickle.load(open('scalar.pkl', 'rb'))
encode1 = pickle.load(open('genlbl.pkl', 'rb'))
encode2 = pickle.load(open('marlbl.pkl', 'rb'))
encode3 = pickle.load(open('worklbl.pkl', 'rb'))
encode4 = pickle.load(open('reslbl.pkl', 'rb'))
encode5 = pickle.load(open('smoklbl.pkl', 'rb'))
class_names = ['Yes','No']
def predict(df):
        df = df[['gender', 'age', 'hypertension', 'heart_disease', 'ever_married','work_type', 'Residence_type', 'avg_glucose_level', 'bmi','smoking_status']]
        df.gender = encode1.transform(df.gender)
        df.ever_married = encode2.transform(df.ever_married)
        df.work_type = encode3.transform(df.work_type)
        df.Residence_type = encode4.transform(df.Residence_type)
        df.smoking_status = encode5.transform(df.smoking_status)
        numpy_array = df.to_numpy()
        # Predict
        
        numpy_array = scaler.transform(numpy_array)
        predictions = model.predict(numpy_array)
        
        #return str(predictions)
        output = [class_names[class_predicted] for class_predicted in predictions]
        return output
