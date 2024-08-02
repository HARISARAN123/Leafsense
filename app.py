import os
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from PIL import Image

app = Flask(__name__)

# Load your model here...
# Define the model architecture
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout

# Create a Sequential model
model = Sequential()

# Add a Conv2D layer with appropriate input shape
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(256, 256, 3)))

# Add a MaxPooling2D layer
model.add(MaxPooling2D(pool_size=(2, 2)))

# Add more Conv2D and MaxPooling2D layers as needed
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

# Flatten the output of the convolutional layers
model.add(Flatten())

# Add a fully connected layer with 1024 units
model.add(Dense(1024, activation='relu'))

# Add a dropout layer for regularization
model.add(Dropout(0.5))

# Add the output layer with appropriate number of units (based on your problem)
model.add(Dense(15, activation='softmax'))

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])




labels = {0: 'Pepper__bell___Bacterial_spot', 1: 'Pepper__bell___healthy', 
          2: 'Potato___Early_blight', 3: 'Potato___Late_blight', 4: 'Potato___healthy', 
          5: 'Tomato_Bacterial_spot', 6: 'Tomato_Early_blight', 7: 'Tomato_Late_blight',
          8: 'Tomato_Leaf_Mold', 9: 'Tomato_Septoria_leaf_spot', 
          10: 'Tomato_Spider_mites_Two_spotted_spider_mite', 11: 'Tomato__Target_Spot', 
          12: 'Tomato__Tomato_YellowLeaf__Curl_Virus', 13: 'Tomato__Tomato_mosaic_virus', 
          14: 'Tomato_healthy'}

# Dictionary mapping disease labels to prevention methods
prevention_methods = {
    'Pepper__bell___Bacterial_spot': 'Apply copper-based fungicides, avoid overhead irrigation, and practice crop rotation.',
    'Pepper__bell___healthy': 'Ensure proper spacing between plants, use disease-resistant varieties, and monitor for signs of disease.',
    'Potato___Early_blight': 'Plant disease-resistant varieties, rotate crops, and remove infected leaves.',
    'Potato___Late_blight': 'Apply fungicides, rotate crops, and remove infected plants and plant parts.',
    'Potato___healthy': 'Practice good sanitation, rotate crops, and monitor for early signs of disease.',
    'Tomato_Bacterial_spot': 'Apply copper-based fungicides, practice crop rotation, and avoid overhead irrigation.',
    'Tomato_Early_blight': 'Remove infected leaves, apply fungicides, and maintain proper plant spacing.',
    'Tomato_Late_blight': 'Practice crop rotation, apply fungicides, and avoid overhead irrigation.',
    'Tomato_Leaf_Mold': 'Use disease-resistant varieties, apply fungicides, and maintain proper air circulation.',
    'Tomato_Septoria_leaf_spot': 'Remove infected leaves, apply fungicides, and maintain proper air circulation.',
    'Tomato_Spider_mites_Two_spotted_spider_mite': 'Apply miticides, prune infected plant parts, and maintain proper humidity levels.',
    'Tomato__Target_Spot': 'Apply fungicides, remove infected leaves, and practice crop rotation.',
    'Tomato__Tomato_YellowLeaf__Curl_Virus': 'Use disease-resistant varieties, control whiteflies, and remove infected plants.',
    'Tomato__Tomato_mosaic_virus': 'Control aphids, use disease-resistant varieties, and remove infected plants.',
    'Tomato_healthy': 'Practice good garden hygiene, rotate crops, and monitor for pests and diseases.'
}

def predict_disease(image_path):
    img = load_img(image_path, target_size=(256, 256))
    x = img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = x.astype('float32') / 255.
    predictions = model.predict(x)[0]
    predicted_label = labels[np.argmax(predictions)]
    prevention_method = prevention_methods.get(predicted_label, "Prevention method not available")
    return predicted_label, prevention_method

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        f = request.files['file']
        if f:
            filename = secure_filename(f.filename)
            file_path = os.path.join('uploads', filename)
            f.save(file_path)
            predicted_label, prevention_method = predict_disease(file_path)
            return render_template('index.html', image_file=file_path, prediction=predicted_label, prevention=prevention_method)
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/team')
def team():
    return render_template('team.html')

if __name__ == '__main__':
    app.run(debug=True)