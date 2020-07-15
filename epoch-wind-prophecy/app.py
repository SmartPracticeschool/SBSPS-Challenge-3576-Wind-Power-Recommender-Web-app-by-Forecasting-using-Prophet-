from flask import Flask,request,render_template, make_response, redirect
import pandas as pd
import pygal
import pickle
from pygal.style import BlueStyle, NeonStyle, DarkStyle

model = pickle.load(open('prophet_new.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/pred')
def pred():
    return render_template('prediction.html')

@app.route('/predict', methods =["POST","GET"]) 
def predict():
    # ============-> Predicting power for values entered by the user <-====================
    date = request.form["date"]
    q = float(request.form["c"])
    p = float(request.form["a"])
    r = float(request.form["b"])

    neq=pd.DataFrame()
    neq = pd.DataFrame([[date,q,p,r]],columns=['ds', 'Pressure | (atm)', 'Wind speed | (m/s)', 'Wind direction | (deg)'],
                                       dtype=float)
     # ===========-> Actual Forecasting <-================== 
    l = model.predict(neq)
    dk=l['yhat']
    out = dk[0]

    return render_template("prediction.html",dks=out)

# @app.route('/tb')
# def tb():
#     return render_template('tb.html')

# @app.route('/table', methods=["POST","GET"])
# def table():

#     return render_template('tables.html')

@app.route('/dash')
def dash():
    return redirect('https://prophecy.eu-gb.mybluemix.net/ui/#!/1?socketid=OAt1qeZth5PB6RjTAAAY')

if __name__ == '__main__':
    app.run(debug=True)