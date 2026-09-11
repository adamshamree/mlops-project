import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score
import pandas as pd
import numpy as np

# Generate fake transaction data
np.random.seed(42)
n = 1000
data = pd.DataFrame({
    'amount': np.random.exponential(1000, n),
    'foreign': np.random.binomial(1, 0.3, n),
    'hour': np.random.randint(0, 24, n),
    'fraud': np.random.binomial(1, 0.1, n)
})

X = data[['amount', 'foreign', 'hour']]
y = data['fraud']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Start MLflow experiment
mlflow.set_experiment("fraud-detection")

with mlflow.start_run():
    # Train model
    model = RandomForestClassifier(n_estimators=100, max_depth=5)
    model.fit(X_train, y_train)

    # Evaluate
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    precision = precision_score(y_test, predictions, zero_division=0)

    # Log to MLflow
    mlflow.log_param("n_estimators", 100)
    mlflow.log_param("max_depth", 5)
    mlflow.log_metric("accuracy", accuracy)
    mlflow.log_metric("precision", precision)
    mlflow.sklearn.log_model(model, "fraud-model")

    print(f"Accuracy: {accuracy:.3f}")
    print(f"Precision: {precision:.3f}")
    print("Model logged to MLflow!")
