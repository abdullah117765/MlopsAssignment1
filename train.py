import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load the Iris dataset and drop the 'Id' column
iris_data = pd.read_csv("./iris.csv").drop("Id", axis=1)

# Split data into features (X) and target labels (y)
X = iris_data.drop("Species", axis=1)
y = iris_data["Species"]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=150)

# Create and train a Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate the model (optional)
accuracy = model.score(X_test, y_test)
print(f"Model Accuracy: {accuracy}")

# Save the trained model to a file
joblib.dump(model, "iris_model.pkl", protocol=4)
