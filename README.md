🫁 Lung Cancer Risk Prediction Web App
A deep learning-powered web application that predicts lung cancer risk levels — Low, Medium, or High — using 23 clinical, lifestyle, and environmental inputs from the user.


🔍 Overview
This project combines a trained MLP deep learning model (using Keras and TensorFlow) with a beautiful Flask web interface. Users enter personal and environmental details, and the app instantly predicts their lung cancer risk.

🎯 Features
🌟 High-end UI with:

Glassmorphism design

Dark/light mode toggle

Scroll & Lottie animations

Responsive layout

🧠 Deep Learning Model:

Multilayer Perceptron (MLP)

Preprocessing with StandardScaler

⚙️ Real-time Prediction using Flask

📊 Training Visualization:

Accuracy & loss graphs

🧪 Testing Mode:

Script to test different inputs

💾 Model Artifacts:

Saved .h5 model and scaler.pkl

🚀 How It Works
📝 User Inputs

Age, Gender, Air pollution, Smoking, Alcohol use, Genetic risk, etc.

⚙️ Preprocessing

Inputs are scaled using StandardScaler

🧠 Prediction

Model predicts: Low, Medium, or High risk

🎨 Output

Risk level shown on a beautifully styled results page

🎨 Tech Stack
Backend: Flask, Python

Model: TensorFlow, Keras (MLP)

Frontend: HTML5, CSS3, JavaScript

Visual Effects: Lottie Animations, AOS (Animate on Scroll), Particles.js

Styling: Bootstrap 5 (optional), Custom Glassmorphism

🗂️ Project Structure
lung-cancer-prediction-using-deep-learning/
│
├── screenshots/                 # UI & result screenshots
│   ├── accuracy_graph.JPG
│   ├── epoch.JPG
│   ├── form.JPG
│   ├── home.JPG
│   └── result.JPG
│
├── templates/                   # Flask HTML templates
│   ├── home.html
│   ├── form.html
│   └── results.html
│
├── cancer_patient_datasets.csv # Dataset
├── gui.py                       # Optional Tkinter GUI
├── test.py                      # Test script with dummy inputs
├── train.py                     # Model training
├── app.py                       # Flask backend
│
├── my_model.h5                  # Trained model
├── scaler.pkl                   # StandardScaler object
│
├── requirements.txt             # Dependencies
├── LICENSE                      # MIT License
├── README.md                    # This file

⚙️ Installation & Running Locally

# Clone the repo
git clone https://github.com/bindu2607/lung-cancer-prediction-using-deep-learning
cd lung-cancer-prediction-using-deep-learning

# (Optional) Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the Flask web app
python app.py
