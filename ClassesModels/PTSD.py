import joblib

class ptsd:
    def __init__(self):
        self.ptsd_model = joblib.load("PTSD.pkl")

    # Function that takes a binary array of size 5 as input and returns the predicted outcome for the PTSD test
    def ptsd_prediction_with_array(self,answers_array):
        prediction = self.ptsd_model.predict([answers_array])
        switcher = {
            0: 'No PTSD',
            1.0: 'PTSD Present'
        }

        return switcher.get(float(prediction[0]), "Wrong Result")

    # Function that takes in 5 binary values as input and returns the predicted outcome for the PTSD test
    def ptsd_prediction_with_values(self,q1, q2, q3, q4, q5):
        prediction = self.ptsd_model.predict([[q1, q2, q3, q4, q5]])
        switcher = {
            0: 'No PTSD',
            1.0: 'PTSD Present'
        }

        return switcher.get(float(prediction[0]), "Wrong Result")