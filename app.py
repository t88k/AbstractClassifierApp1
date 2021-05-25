from flask import Flask,render_template,url_for,request
import joblib
from textpreprocessing import pre_process


topics = {1:'Computer Science', 2:'Physics', 3:'Mathematics', 4:'Statistics', 5:'Quantitative Biology', 6:'Quantitative Finance'}

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
	abstract = request.form['message']
	prediction = pipeline.predict([abstract])

	topic_prediction = topics[prediction[0]]

	return render_template('result.html', prediction=topic_prediction)


if __name__ == '__main__':
	
	pipeline = joblib.load('abstract_classification.joblib')
	app.run()
