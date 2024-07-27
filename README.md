# Crop Disease Detection Model

This repository contains an integrated real-time TensorFlow Lite model for detecting diseases in crop leaves, specifically for tomato and wheat plants.

## Overview

The `imageModel` class in this project provides functionality to:
1. Predict diseases in crop leaves from an image
2. Predict diseases in crop leaves from a directory of images

The model can detect the following conditions:
- Tomato Leaf Early Blight
- Healthy Tomato Leaf
- Tomato Leaf Late Blight
- Healthy Wheat Leaf
- Wheat Leaf Septoria
- Wheat Leaf Stripe Rust

## Usage

### Initializing the Model

```python
model = imageModel()
```

This will load the TensorFlow Lite model from the file `cropDiseaseModel.tflite`.

### Predicting Disease for a Single Image

```python
result = model.predict_single_image("path/to/your/image.jpg")
print(result)
```

This will return a dictionary with the input path and the predicted disease.

### Predicting Diseases for Multiple Images in a Directory

```python
result = model.predict_image_directory("path/to/your/image/directory")
print(result)
```

This will return a dictionary with the input directory and predictions for all images in that directory.

