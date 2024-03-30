from flask import Flask, request, render_template
import joblib
import os

app = Flask(__name__)

model = joblib.load("iris_model.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        sepal_length = float(request.form["sepal_length"])
        sepal_width = float(request.form["sepal_width"])
        petal_length = float(request.form["petal_length"])
        petal_width = float(request.form["petal_width"])

        # Include all features, even if some aren't used for prediction
        input_features = [[sepal_length, sepal_width, petal_length, petal_width, 0]]  # Assuming 'Species' isn't used for prediction
        prediction = model.predict(input_features)[0]

        return render_template("index.html", prediction=prediction)

    return render_template("index.html", prediction=None)

if __name__ == "__main__":
    app.run(debug=True)
