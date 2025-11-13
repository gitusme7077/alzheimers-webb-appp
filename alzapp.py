import os
import numpy as np
from flask import Flask, request, render_template_string

# Initialize Flask app
app = Flask(__name__)

# Dummy model class for demonstration
class DummyModel:
    def predict(self, features):
        # Simple logic: if mean > 0, predict Alzheimer's (1); else Healthy (0)
        if np.mean(features[0]) > 0:
            return [1]
        else:
            return [0]

# Create an instance of DummyModel
model = DummyModel()

# HTML template
HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Alzheimer's Prediction App</title>
</head>
<body>
    <h1>Predict Health Status</h1>
    <form method="POST">
        <button type="submit">Generate Signal and Predict</button>
    </form>
    {% if result %}
        <h2>Prediction Result: {{ result }}</h2>
    {% endif %}
</body>
</html>
"""

# Define route
@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        # Generate a random signal
        signal = np.random.randn(128)
        # Calculate features
        features = [np.mean(signal), np.std(signal), np.max(signal), np.min(signal)]
        # Make prediction
        prediction = model.predict([features])[0]
        result = "Alzheimer's" if prediction == 1 else "Healthy"
    return render_template_string(HTML, result=result)

# Run the app
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
  

