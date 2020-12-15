import pickle
import numpy as np
import flask

app = flask.Flask(__name__)
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)


@app.route('/')
def home():
    return flask.render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    """"""
    int_features = [int(x) for x in flask.request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = round(prediction[0], 2)

    return flask.render_template('index.html', prediction_text=f'Employee salary should be $ {output:.2f}')


if __name__ == '__main__':
    app.run(debug=True)
