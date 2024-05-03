from flask import Flask, request, render_template
import sklearn
import pickle
import pandas as pd
import numpy as np


app = Flask(__name__)

pickle_file = pickle.load(open("liver.pkl", "rb"))

@app.route("/")
# @cross_origin()
def index():
    return render_template("index.html")

@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        age = int(request.form['age'])
        n_days = int(request.form['n_days'])
        drug = int(request.form['drug'])
        sex = int(request.form['sex'])
        ascites = int(request.form['ascites'])
        hepatomegaly = int(request.form['hepatomegaly'])
        spiders = int(request.form['spiders'])
        bilirubin = float(request.form['bilirubin'])
        cholesterol = float(request.form['cholesterol'])
        albumin = float(request.form['albumin'])
        copper = float(request.form['copper'])
        alk_Phos = float(request.form['alk_Phos'])
        sgot = float(request.form['sgot'])
        tryglicerides = float(request.form['tryglicerides'])
        platelets = float(request.form['platelets'])
        prothrombin = float(request.form['prothrombin'])
        stage = int(request.form['stage'])
        edema = int(request.form['edema'])

        data = np.array([[age, n_days, drug, sex, ascites, hepatomegaly, spiders, bilirubin, cholesterol, albumin, copper, alk_Phos, sgot, tryglicerides, platelets, prothrombin, stage, edema]])
        prediction = pickle_file.predict(data)

        return render_template('predict.html', prediction=prediction)  

if __name__ == "__main__":
    app.run(debug=True)
