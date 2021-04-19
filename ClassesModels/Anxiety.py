import joblib
import pickle


class anxiety:
    def __init__(self):
        self.anxiety_model = joblib.load(
            "/media/raza/asd/Django/test/MindBliss/ClassesModels/anxiety.pkl")
        print(self.anxiety_model)

    # Function that takes a binary array of size 7 as input and returns the predicted outcome for the Anxiety test
    def anxiety_prediction_with_array(self, answers_array):
        prediction = self.anxiety_model.predict([answers_array])
        switcher = {
            0: 'No Anxiety',
            0.3: 'Minor Anxiety',
            0.6: 'Moderate Anxiety',
            1.0: 'Severe Anxiety'
        }

        return switcher.get(float(prediction[0]), "Wrong Result")

    # Function that takes in 7 binary values as input and returns the predicted outcome for the Anxiety test
    def anxiety_prediction_with_values(self, q1, q2, q3, q4, q5, q6, q7):
        prediction = self.anxiety_model.predict([[q1, q2, q3, q4, q5, q6, q7]])
        switcher = {
            0: 'No Anxiety',
            0.3: 'Minor Anxiety',
            0.6: 'Moderate Anxiety',
            1.0: 'Severe Anxiety'
        }

        return switcher.get(float(prediction[0]), "Wrong Result")
