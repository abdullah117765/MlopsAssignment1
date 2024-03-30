from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load("iris_model.pkl")


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            data = request.get_json()
            features = [
                data['sepal_length'], data['sepal_width'],
                data['petal_length'], data['petal_width']
            ]
            prediction = model.predict([features])
            return jsonify({'prediction': prediction[0]})
        except Exception as e:
            return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True)
