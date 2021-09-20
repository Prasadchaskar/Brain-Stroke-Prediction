import pickle
import numpy as np
import pandas as pd
model = pickle.load(open('stroke.pkl', 'rb'))
scaler = pickle.load(open('scalar.pkl', 'rb'))
class_names = ['Yes','No']
def predict(df):
        df = df[['gender', 'age', 'hypertension', 'heart_disease', 'ever_married','work_type', 'Residence_type', 'avg_glucose_level', 'bmi','smoking_status']]
        numpy_array = df.to_numpy()
        # Predict
        numpy_array = scaler.transform(numpy_array)
        predictions = model.predict(numpy_array)
        
        #return str(predictions)
        output = [class_names[class_predicted] for class_predicted in predictions]
        return output
