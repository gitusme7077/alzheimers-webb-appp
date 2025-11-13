import numpy as np
from flask import Flask, request, render_template_string
import pickle # Recommended for loading real models

# 1. Initialize the Flask app
app = Flask(__name__)

# 2. Define a placeholder model
# In a real application, you would load a trained model like this:
# with open('your_model.pkl', 'rb') as f:
#     model = pickle.load(f)

# For demonstration, we create a simple "dummy" model class
class DummyModel:
    def predict(self, features):
        # A simple logic: if mean > 0, predict 1 (Alzheimer's), otherwise 0 (Healthy)
        # This is just so the code runs without error.
        if np.mean(features[0]) > 0:
            return [1]
        else:
            return [0]

model = DummyModel()

# 3. Define the HTML template string
HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Alzheimer's Prediction App</title>
</head>
<body>
    <h1>Predict Health Status</h1>
    <form method="POST">
        <!-- In a real app, you would have input fields for features -->
        <button type="submit">Generate Signal and Predict</button>
    </form>
    {% if result %}
        <h2>Prediction Result: {{ result }}</h2>
    {% endif %}
</body>
</html>
"""

# 4. Define the route
@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        # In a real application, you might get features from form inputs:
        # feature1 = float(request.form['feature1'])
        # features = [feature1, ...]

        # Using the provided random signal for this example
        signal = np.random.randn(128)
        features = [np.mean(signal), np.std(signal), np.max(signal), np.min(signal)]

        # The model expects a list of samples, so [features] is correct
        prediction = model.predict([features])[0]
        result = "Alzheimer's" if prediction == 1 else "Healthy"
    return render_template_string(HTML, result=result)

# 5. Run the application
if __name__ == "__main__":
    # In a production environment (like Render), Flask automatically handles
    # host and port if you use a service like Gunicorn.
    # For local testing, this is fine:
    app.run(debug=True)
