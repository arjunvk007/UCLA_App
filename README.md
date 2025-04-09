# Neural Network Predicting Chances of Admission at UCLA 

This Streamlit application predicts the likelihood of admission to UCLA based on academic profile inputs using a trained neural network model.

---

## 📌 Overview

The UCLA Admission Predictor is a machine learning application that estimates a student's chance of admission to UCLA based on various academic factors including GRE scores, TOEFL scores, university rating, SOP strength, LOR strength, CGPA, and research experience.
---

## 🛠 Project Structure

```
├── app.py 
├── train.py 
├── data_preprocessing.py 
├── evaluate_model.py 
├── logger.py 
├── models/
│ └── admission_nn_model.pkl
├── data/
│ └── Admission(in).csv
└── requirements.txt

---

## 🚀 How to Run

```bash
git clone [repository-url]
cd ucla-admission-predictor

### 🌐 Step 2: Set Up a Virtual Environment

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

### 📦 Step 3: Install Dependencies

pip install -r requirements.txt

### ▶️ Step 4: Run the Streamlit App

streamlit run app.py

## 🎯 Features

- Interactive web interface with sliders and input fields

- Real-time admission chance prediction

- Clear visualization of prediction results

- Responsive design for different screen sizes

---

## 🗃 Data

GRE Score (260-340)

TOEFL Score (0-120)

University Rating (1-5)

SOP Strength (1-5)

LOR Strength (1-5)

CGPA (6.0-10.0)

Research Experience (Yes/No)

Admission Chance (0.0-1.0)

---

## 📈 Technologies Used

Python 

Streamlit 

Scikit-learn 

Pandas

Joblib

NumPy

---

## 🌩 Deployment

Local Environment: http://localhost:8501/
Git hub: https://uclaapp-arjunvk.streamlit.app/
---

## 📜 License

Licensed under the [MIT License](LICENSE).

---

## 🙌 Contribution

Feel free to fork this repository and make improvements or adjustments. Pull requests and contributions are always welcome!

---

## ✉️ Contact

- **Author:** Arjun Vannathan Kandy
- **GitHub:** https://github.com/arjunvk007/
 
