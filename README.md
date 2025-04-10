# 🫁 Lung Cancer Risk Prediction Web App

A deep learning-powered web application that predicts lung cancer risk level (Low, Medium, High) based on 23 clinical, lifestyle, and environmental features provided by the user.

---

## 🔍 Overview

This project integrates a trained deep learning model (using Keras and TensorFlow) with a Flask-based web interface to provide real-time lung cancer risk predictions. Users input their health and environmental data, and the model predicts the probability level of lung cancer risk.

---

## 🖥️ Features

- ✅ High-end UI with **glassmorphism**, **dark/light mode toggle**, **Lottie animations**, **scroll animations**, and **responsive layout**
- 🧠 Trained deep learning model using **Multilayer Perceptron (MLP)**
- 🔥 Real-time predictions with Flask backend
- 📊 Visualized accuracy and loss graphs
- 🧪 Testing script for trying different input combinations
- 📦 Saved scaler and trained model (`.h5`, `.pkl`)

---

## 🚀 How It Works

1. **User Inputs**:
   - Age, Gender
   - Air pollution, Alcohol use, Smoking, Genetic risk, etc.
2. **Preprocessing**:
   - Data scaled using `StandardScaler`
3. **Prediction**:
   - Model predicts risk level: Low / Medium / High
4. **Output**:
   - Result displayed on a beautifully styled results page

---

## 📁 Project Structure

```bash
lung-cancer-prediction-using-deep-learning/
│
├── screenshots/                 # UI & result screenshots
│   ├── accuracy_graph.JPG
│   ├── epoch.JPG
│   ├── form.JPG
│   ├── home.JPG
│   └── result.JPG
│
├── templates/                   # HTML templates for Flask
│   ├── form.html
│   ├── home.html
│   └── results.html
│
├── cancer_patient_datasets.csv # Lung cancer dataset
├── gui.py                       # Optional Tkinter GUI script
├── test.py                      # Test script with dummy inputs
├── train.py                     # Model training script
├── app.py                       # Flask web application
│
├── my_model.h5                  # Trained Keras model
├── scaler.pkl                   # Saved StandardScaler
│
├── requirements.txt             # Python dependencies
├── LICENSE                      # MIT License
├── README.md                    # Project documentation
├── package-lock.json            # Frontend dependencies (optional)


## 📦 Installation & Running Locally

```bash
# Clone the repo
git clone https://github.com/bindu2607/lung-cancer-prediction-using-deep-learning
cd lung-cancer-prediction-using-deep-learning

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install required packages
pip install -r requirements.txt

# Run the Flask app
python app.py

## 🎨 UI Technologies Used

Flask + Jinja2
HTML5 / CSS3 / JavaScript
Lottie Animations
AOS (Animate On Scroll)
Particles.js
Bootstrap 5 (optional, if included)
