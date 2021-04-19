import joblib

class bipolar:
    def __init__(self):
        self.bipolar_model = joblib.load(
            "/media/raza/asd/Django/test/MindBliss/ClassesModels/bipolar.pkl")


    # Function that takes a binary array of size 11 as input and returns the predicted outcome for the bipolar test
    def bipolar_prediction_with_array(self,answers_array):
        prediction = self.bipolar_model.predict([answers_array])
        switcher = {
             0: 'Negative bipolar',
            1.0: 'Positive bipolar' 
        }

        return switcher.get(float(prediction[0]), "Wrong Result")

    # Function that takes in 11 binary values as input and returns the predicted outcome for the bipolar test
    def bipolar_prediction_with_values(self,q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11):
        prediction = self.bipolar_model.predict([[q1, q2, q3, q4, q5, q6, q7, q8 ,q9, q10, q11]])
        switcher = {
            0: 'Negative bipolar',
            1.0: 'Positive bipolar'
        }

        return switcher.get(float(prediction[0]), "Wrong Result")
