# Handwritten Digit Recognition

A simple neural network using TensorFlow to recognize handwritten digits from the MNIST dataset.

---

## 🛠 Installation

1. **Install Python 3.9.11**

   Download from the official [Python Downloads](https://www.python.org/downloads/release/python-3911/) page.

2. **Install dependencies**

   Open a terminal and run:

   ```bash
   pip install numpy matplotlib tensorflow opencv-python
````

---

## 🚀 Usage

1. **Train the model**

   ```bash
   python train.py
   ```

   This will train the model and save it as `Handwritten_detection.keras`.

2. **Use the trained model with your image**

   ```bash
   python use.py --file=C://Users/Image.png
   ```

   Replace the path with your own image file (must be 28x28 grayscale or a similar digit).
---

## 📝 Notes

* Make sure the image background is white and the digit is dark for best results.
* The model is based on the MNIST dataset (28x28 pixels).