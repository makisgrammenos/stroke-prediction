from flask import Flask, request, jsonify, json, Response, render_template
import os
from predict import predict
app = Flask(__name__)


@app.route("/")
def main():
    return "Test"
@app.route("/predict",methods=['POST'])
def predict_results():
    data = request.get_json()
    template =  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    #template =  [62, 1, 0, 0, 0, 0, 1, 1, 100, 28, 0, 0, 0, 1, 0, 0, 0, 1, 0]


    template[0] = data["age"]

    if (data['gender'] =='Male'):
        template[1] = 1
    elif (data['gender'] == "Female"):
        template[2] =1
    elif (data['gender'] =="Other"):
        template[3] = 1

    template[4] = 1 if data['hypertension'] == "Yes" else 0

    template [5] = 1 if data['heart_disease'] == "Yes" else 0

    template[6] = 1 if data['ever_married'] == "Yes" else 0

    template[7] = 1 if data['residence_type'] =="Rural" else 0

    template[8] = float(data['avg_glucose'])

    template[9] = float(data['bmi'])

    if data['job_type']  == "Government":
        template[10] = 1
    elif data['job_type'] == "Never worked":
        template[11] = 1
    elif data['job_type'] == "Private":
        template[12] = 1
    elif data['job_type'] =="Self-employed":
        template[13] = 1
    elif data['job_type'] == "Children":
        template[14] =1

    if data['smoking_status'] == "Unknown":
        template[15]=1
    elif data['smoking_status'] =="Formerly smoked":
        template[16] =1
    elif data['smoking_status'] =="Never smoked":
        template[17] =1
    elif data['smoking_status'] =="Smokes":
        template[18] =1

    try:
        prediction = predict(template)
    except Exception as e:
        return Exception , 400

    return jsonify(prediction)

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)