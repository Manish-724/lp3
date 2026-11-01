# Practical 2: Multiclass Letter Recognition using a Deep Neural Network
# Install: pip install numpy tensorflow scikit-learn
# OpenML/network access is required to fetch the dataset.
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.datasets import fetch_openml

print("Loading Letter Recognition dataset...")
letter_data = fetch_openml(name="letter", version=1, as_frame=True)
X = letter_data.data.astype(float)
y = letter_data.target

# Convert letters A-Z into numeric labels and one-hot encode them
encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)
y_onehot = to_categorical(y_encoded, num_classes=26)

X_train, X_test, y_train, y_test = train_test_split(
    X, y_onehot, test_size=0.2, random_state=42
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = Sequential([
    Dense(128, activation="relu", input_shape=(X_train_scaled.shape[1],)),
    Dropout(0.3),
    Dense(64, activation="relu"),
    Dropout(0.3),
    Dense(26, activation="softmax")
])

model.compile(optimizer="adam", loss="categorical_crossentropy",
              metrics=["accuracy"])

print("Training the Deep Neural Network...")
model.fit(X_train_scaled, y_train, epochs=50, batch_size=32,
          validation_split=0.2, verbose=1)

loss, accuracy = model.evaluate(X_test_scaled, y_test, verbose=0)
print("Test accuracy:", accuracy)

probabilities = model.predict(X_test_scaled[:5], verbose=0)
predicted_letters = encoder.inverse_transform(probabilities.argmax(axis=1))
print("Predicted letters:", predicted_letters)
