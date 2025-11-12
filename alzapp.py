from flask import Flask, request, render_template_string
import numpy as np
from sklearn.svm import SVC

app = Flask(__name__)

# Load preprocessed data
X = np.load("features.npy")
y = np.load("labels.npy")

# Train model
model = SVC(kernel='linear')
model.fit(X, y)

# HTML template
HTML = """
<!doctype html>
<html>
<head>
    <title>Alzheimer's Detection</title>
</head>
<body style="font-family: Arial; text-align: center; margin-top: 50px;">
    <h2>Alzheimer's Detection from Simulated EEG</h2>
    <form method="POST">
        <button type="submit" style="padding: 10px 20px; font-size: 16px;">Simulate EEG & Predict</button>
    </form>
    {% if result %}
        <h3 style="margin-top: 30px;">Prediction: {{ result }}</h3>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        signal = np.random.randn(128)
        features = [np.mean(signal), np.std(signal), np.max(signal), np.min(signal)]
        prediction = model.predict([features])[0]
        result = "Alzheimer's" if prediction == 1 else "Healthy"
    return render_template_string(HTML, result=result)

if __name__ == "__main__":
    app.run(debug=True)