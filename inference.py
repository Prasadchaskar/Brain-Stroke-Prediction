import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
scalr = StandardScaler()
model = pickle.load(open('stroke.pkl', 'rb'))
class_names = ['Yes','No']

def predict(df):
        df = df[['gender', 'age', 'hypertension', 'heart_disease', 'ever_married',
        'work_type', 'Residence_type', 'avg_glucose_level', 'bmi',
        'smoking_status']]

        numpy_array = df.to_numpy()
        numpy_array = scalr.fit_transform(numpy_array)
        # Predict
        predictions = model.predict(numpy_array)
        #return str(predictions)
        output = [class_names[class_predicted] for class_predicted in predictions]
        return output
