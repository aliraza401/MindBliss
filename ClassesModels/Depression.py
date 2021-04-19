import joblib

class depression:
    def __init__(self):
        self.depression_model = joblib.load("depression.pkl")

    # Function that takes a binary array of size 10 as input and returns the predicted outcome for the Depression test
    def depression_prediction_with_array(self,answers_array):
        prediction = self.depression_model.predict([answers_array])
        switcher = {
            0: 'No Depression',
            0.3: 'Mild Depression',
            0.6: 'Moderate Depression',
            1.0: 'Severe Depression'
        }

        return switcher.get(float(prediction[0]), "Wrong Result")

    # Function that takes in 10 binary values as input and returns the predicted outcome for the Depression test
    def depression_prediction_with_values(self,q1, q2, q3, q4, q5, q6, q7, q8, q9, q10):
        prediction = self.depression_model.predict([[q1, q2, q3, q4, q5, q6, q7, q8 ,q9, q10]])
        switcher = {
            0: 'No Depression',
            0.3: 'Mild Depression',
            0.6: 'Moderate Depression',
            1.0: 'Severe Depression'
        }

        return switcher.get(float(prediction[0]), "Wrong Result")