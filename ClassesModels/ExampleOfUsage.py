# An Example of how to use the mental health predictors
from Anxiety import anxiety

anxiety = anxiety()

Input_from_some_form = [1, 1, 0, 1, 1, 0, 0]

prediction = anxiety.anxiety_prediction_with_array(Input_from_some_form)


print(prediction)


