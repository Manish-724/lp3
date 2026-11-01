# Practical 1: Boston Housing Price Prediction using a Deep Neural Network
# Install: pip install numpy pandas tensorflow scikit-learn
# Note: OpenML availability/network access is required to fetch this dataset.
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import fetch_openml

print("Loading Boston Housing dataset...")
boston = fetch_openml(name="boston", version=1, as_frame=True)
X = boston.data.astype(float)
y = boston.target.astype(float)

# Split into 80% training and 20% testing data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Feature scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Build the neural network
model = Sequential([
    Dense(64, activation="relu", input_shape=(X_train_scaled.shape[1],)),
    Dense(32, activation="relu"),
    Dense(1)  # One continuous house-price prediction
])

# Compile and train
model.compile(optimizer="adam", loss="mean_squared_error", metrics=["mae"])
model.fit(X_train_scaled, y_train, epochs=100, batch_size=32,
          validation_split=0.2, verbose=1)

# Evaluate and predict
loss, mae = model.evaluate(X_test_scaled, y_test, verbose=0)
print("Test Mean Absolute Error:", mae)
predictions = model.predict(X_test_scaled[:5], verbose=0)
print("First five predicted prices:", predictions.flatten())
print("Actual prices:", np.asarray(y_test[:5]))
