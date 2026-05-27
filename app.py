from flask import Flask,render_template,request,redirect
import pickle as pk
import pandas  as pd
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)
scaler = pk.load(open("scaler.pkl","rb"))
logisticreg = pk.load(open("logisticreg.pkl","rb"))
geo_encode = pk.load(open("geo_encode.pkl","rb"))
gender_encode = pk.load(open("gender_encode.pkl","rb"))

# xgboost = pk.load(open("xgboost.pkl","rb"))
# ann = pk.load(open("ann.pkl","rb"))
setData = []
@app.route("/")
def viewpage():
     # return "Hello world"
     return render_template("index.html",setData = setData,prediction_text ="")
@app.route("/addData")
def addData():
       cdscore = request.args.get("cdscore")
       geo = request.args.get("geo")
       gender = request.args.get("gender")
       age = request.args.get("age")
       tenure = request.args.get("tenure")
       balance = request.args.get("balance")
       numproduct = request.args.get("numproduct")
       hascr = request.args.get("hascr")
       isactive = request.args.get("isactive")
       salary = request.args.get("salary")
       data = {
          "CreditScore": cdscore,
          "Geography": geo,
          "Gender": gender,
          "Age": age,
           "Tenure": tenure,
          "Balance": balance,
          "NumOfProducts": numproduct,
          "HasCrCard": hascr,
          "IsActiveMember": isactive,
          "EstimatedSalary": salary }
      #  setData.append(float(data))
       pred_data = pd.DataFrame([data])
       print(pred_data)
       pred_data['Geography'] =geo_encode.transform( pred_data['Geography'])
       pred_data['Gender'] = gender_encode.transform(pred_data['Gender'])
       pred_data['HasCrCard'] = pred_data['HasCrCard'].map({'Yes':1,'No':0})
       pred_data['IsActiveMember'] = pred_data['IsActiveMember'].map({'Yes':1,'No':0})


       pred_data = scaler.transform(pred_data)

       prediction = logisticreg.predict(pred_data)

       if prediction[0] == 1:
          result = "Customer will leave"
       else:
          result = "Customer will stay"

       return render_template("index.html",scaler = scaler,gender_encode = gender_encode,geo_encode = geo_encode,logisticreg = logisticreg, prediction_text=result)


