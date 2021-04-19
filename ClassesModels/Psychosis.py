import joblib

class psychosis:
    def __init__(self):
        self.psychosis_model = joblib.load("psychosis.pkl")

    # Function that takes a binary array of size 15 as input and returns the predicted outcome for the Psychosis test
    def psychosis_prediction_with_array(self,answers_array):
        prediction = self.psychosis_model.predict([answers_array])
        switcher = {
             0: 'No/Low Risk of Psychosis',
            1.0: 'High Risk of Psychosis'
        }

        return switcher.get(float(prediction[0]), "Wrong Result")

    # Function that takes in 15 binary values as input and returns the predicted outcome for the Psychosis test
    def psychosis_prediction_with_values(self,q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15):
        prediction = self.psychosis_model.predict([[q1, q2, q3, q4, q5, q6, q7, q8 ,q9, q10, q11, q12, q13, q14, q15]])
        switcher = {
              0: 'No/Low Risk of Psychosis',
            1.0: 'High Risk of Psychosis'
        }

        return switcher.get(float(prediction[0]), "Wrong Result")