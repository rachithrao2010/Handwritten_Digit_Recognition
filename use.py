import cv2
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import argparse
import os

# Parse the command line argument
parser = argparse.ArgumentParser(description="Predict digit from image file.")
parser.add_argument('--file', type=str, required=True, help="Path to the image file.")
args = parser.parse_args()

# Load the model
model = tf.keras.models.load_model("model.keras")

# Check if file exists
if not os.path.exists(args.file):
    print(f"File not found: {args.file}")
    exit()

# Read and process the image
img = cv2.imread(args.file, cv2.IMREAD_GRAYSCALE)
if img is None:
    print(f"Unable to read image: {args.file}")
    exit()

img = cv2.resize(img, (28, 28))  # Ensure correct shape
img = np.invert(np.array([img]))  # Invert and wrap in list
img = img / 255.0  # Normalize

# Predict
prediction = model.predict(img)
print(f"The digit was probably a {np.argmax(prediction)}")

# Display image
plt.imshow(img[0], cmap=plt.cm.binary)
plt.title(f"Predicted: {np.argmax(prediction)}")
plt.show()
