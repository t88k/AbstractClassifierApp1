from flask import Flask,render_template,url_for,request
import joblib



topics = {1:'Computer Science', 2:'Physics', 3:'Mathematics', 4:'Statistics', 5:'Quantitative Biology', 6:'Quantitative Finance'}

app = Flask(__name__)

def pre_process(text):
  #Make lowercase
  text = text.strip().lower()

  #Remove punctuation
  filters = '!"\'#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n'
  translate_dict = dict((c, " ") for c in filters)
  translate_map = str.maketrans(translate_dict)
  text = text.translate(translate_map)

  return text

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
	pre_process = pre_process()
	pipeline = joblib.load('abstract_classification.joblib')
	app.run(debug=True)
