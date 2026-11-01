# Practical 3: Fashion MNIST Image Classification using CNN
# Install: pip install tensorflow numpy
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.datasets import fashion_mnist

print("Loading Fashion MNIST dataset...")
(X_train, y_train), (X_test, y_test) = fashion_mnist.load_data()

# Normalize pixels to the range 0 to 1
X_train = X_train.astype("float32") / 255.0
X_test = X_test.astype("float32") / 255.0

# Add one color channel: 28 x 28 x 1
X_train = X_train.reshape(-1, 28, 28, 1)
X_test = X_test.reshape(-1, 28, 28, 1)

class_names = [
    "T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
    "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"
]

model = Sequential([
    Conv2D(32, kernel_size=(3, 3), activation="relu",
           input_shape=(28, 28, 1)),
    MaxPooling2D(pool_size=(2, 2)),
    Conv2D(64, kernel_size=(3, 3), activation="relu"),
    MaxPooling2D(pool_size=(2, 2)),
    Flatten(),
    Dense(128, activation="relu"),
    Dense(10, activation="softmax")
])

model.compile(optimizer="adam",
              loss="sparse_categorical_crossentropy",
              metrics=["accuracy"])

model.fit(X_train, y_train, epochs=5, batch_size=64,
          validation_split=0.1, verbose=1)

loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
print("Test accuracy:", accuracy)

predictions = model.predict(X_test[:10], verbose=0).argmax(axis=1)
for i, prediction in enumerate(predictions):
    print(f"Image {i + 1}: predicted {class_names[prediction]}, "
          f"actual {class_names[y_test[i]]}")
