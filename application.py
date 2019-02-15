from flask import Flask, render_template, request, jsonify
import numpy as np
import pickle

app = Flask(__name__)

def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1,1)
    loaded_model = pickle.load(open("model1.pkl","rb"))
    result = loaded_model.predict(to_predict)
    return result[0]


@app.route('/result',methods = ['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list=list(to_predict_list.values())
        to_predict_list = list(map(int, to_predict_list))
        prediction = ValuePredictor(to_predict_list)

        
        return render_template("result.html",prediction=prediction)



@app.route('/')
def index():
	return render_template('salary.html')

if __name__ =='__main__':
	app.run(debug=True)
