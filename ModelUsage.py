import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import matplotlib.pyplot as plt

model = tf.keras.models.load_model('Gender_Classification_Model_by_Pratz.h5')  


model.compile(loss='binary_crossentropy',
              optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
              metrics=['accuracy'])

def preprocess_and_predict(img_path, model):
    img = image.load_img(img_path, target_size=(150, 150))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0
    prediction = model.predict(img_array)
    confidence = prediction[0][0] 
    if confidence >= 0.5:
        result = 'Male'
    else:
        result = 'Female'
    
    return result, confidence
new_image_path = #path to image
result, confidence = preprocess_and_predict(new_image_path, model)
print(f'The predicted gender is: {result} with confidence: {confidence:.2f}')

img = image.load_img(new_image_path)
plt.imshow(img)
plt.title(f'Predicted: {result} ({confidence:.2f})')
plt.axis('off')
plt.show()
