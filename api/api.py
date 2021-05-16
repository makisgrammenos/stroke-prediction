from flask import Flask, request, jsonify, json, Response, render_template


app = Flask(__name__)


@app.route("/predict",methods=['POST'])
def predict_results():
    data = request.get_json()
    # template =  [62, 1, 0, 0, 0, 0, 1, 1, 100, 28, 0, 0, 0, 1, 0, 0, 0, 1, 0]
    template =  [62, 1, 0, 0, 0, 0, 1, 1, 100, 28, 0, 0, 0, 1, 0, 0, 0, 1, 0]
    if (data['gender'] =='Male'):
        template[1] = 1
    elif (data['gender'] == "Female"):
        template[2] =1
    elif (data['gender'] =="Other"):
        template[3] = 1

    template[4] = 1 if data['hypertension'] == "Yes"

    template [5] = 1 if data['heart_disease'] == "Yes"
