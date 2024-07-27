import cv2, os
import numpy as np
import tensorflow as tf
from keras.utils import img_to_array

class imageModel:
  def __init__(self) -> None:
    self.all_labels = ['Tomato Leaf Early Blight', 'Healthy Tomato Leaf', 'Tomato Leaf Late Blight', 'Healthy Wheat Leaf', 'Wheat Leaf Septoria', 'Wheat Leaf Stripe Rust']
    self.model, self.input_details, self.output_details = self.initalise_model()
  
  def initalise_model(self):
    interpreter = tf.lite.Interpreter(model_path="./cropDiseaseModel.tflite")
    interpreter.allocate_tensors()

    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    return interpreter, input_details, output_details

  def convert_image_to_array(self, image_path):
    try:
      image = cv2.imread(image_path)
      if image is not None:
        image = cv2.resize(image, (224,224)) 
        image_array =  img_to_array(image)
        image_array = np.array(image_array, dtype = np.float32) / 255
        image_array = image_array.reshape(-1, 224, 224, 3)
        return image_array
      else:
        return np.array([])
    except Exception as e:
      print(f"Error : {e}")
      return None
    
  def process_image(self, inputImageDir):
    interpreter = self.model
    input_details = self.input_details
    output_details = self.output_details

    inputImage = self.convert_image_to_array(inputImageDir)
    
    interpreter.set_tensor(input_details[0]['index'], inputImage)
    interpreter.invoke()

    prediction = interpreter.get_tensor(output_details[0]['index'])

    return self.all_labels[np.argmax(prediction)]
  
  def predict_single_image(self, inputPath):
    prediction = self.process_image(inputPath)
    
    result = {
      "input_directory": inputPath,
      "prediction": prediction
    }
    
    return result
  
  def predict_image_directory(self, inputDirectory):
    images = os.listdir(inputDirectory)
    predictions = {}
    
    for idx, image in enumerate(images):
      image_path = os.path.join(inputDirectory, image)
      prediction = self.process_image(image_path)
      predictions[idx] = prediction
    
    result = {
      "input_directory": inputDirectory,
      "predictions": predictions
    }
    
    return result