# 🏦 Smart Lender – Loan Eligibility Prediction Using Machine Learning

## 📌 Project Overview

Smart Lender is a Machine Learning-based web application developed to predict loan eligibility based on applicant information. The system analyzes personal and financial details entered by the user and predicts whether the loan application is likely to be approved or rejected.

The project automates the loan screening process using a trained Random Forest Classifier integrated with a Flask web application, providing quick and reliable predictions through a simple web interface.

---

# 🎯 Objectives

- Automate the loan eligibility prediction process.
- Predict loan approval using Machine Learning.
- Reduce manual effort in loan screening.
- Provide a simple and user-friendly web application.
- Deploy the trained model using Flask.

---

# ✨ Features

- Loan applicant data preprocessing
- Missing value handling
- Feature encoding
- Exploratory Data Analysis (EDA)
- Machine Learning model training
- Model performance evaluation
- Real-time loan eligibility prediction
- Flask-based web application
- Interactive user interface

---

# 🛠 Technology Stack

### Programming Language
- Python

### Machine Learning Libraries
- Pandas
- NumPy
- Scikit-learn
- Pickle

### Visualization Libraries
- Matplotlib
- Seaborn

### Web Technologies
- Flask
- HTML5
- CSS3

### Development Tools
- Google Colab
- Visual Studio Code
- GitHub

---

# 🤖 Machine Learning Model

The project evaluates multiple machine learning algorithms and selects the best-performing model.

### Models Evaluated

- Decision Tree
- K-Nearest Neighbors (KNN)
- Random Forest
- XGBoost

### Final Model

**Random Forest Classifier**

The trained model is saved as:

```
loan_model.pkl
```

---

# 🔄 Development Workflow

```
Loan Dataset
      │
      ▼
Data Preprocessing
      │
      ▼
Missing Value Handling
      │
      ▼
Feature Encoding
      │
      ▼
Exploratory Data Analysis
      │
      ▼
Model Training
      │
      ▼
Model Evaluation
      │
      ▼
Random Forest Selection
      │
      ▼
Model Serialization (loan_model.pkl)
      │
      ▼
Flask Web Application
      │
      ▼
Loan Eligibility Prediction
```

---

# 📂 Project Structure

```
Smart_Lender
│
├── Dataset
│   └── loan_prediction.csv
│
├── Training
│   └── SmartLender_Model_Training.ipynb
│
├── Flask
│   ├── app.py
│   ├── loan_model.pkl
│   ├── requirements.txt
│   │
│   ├── static
│   │     ├── style.css
│   │     └── images
│   │
│   └── templates
│         ├── home.html
│         ├── index.html
│         └── result.html
│
└── README.md
```

---

# ⚙ Functional Modules

- Dataset Loading
- Data Cleaning
- Missing Value Handling
- Feature Encoding
- Exploratory Data Analysis
- Model Training
- Model Evaluation
- Loan Eligibility Prediction
- Flask Application Deployment

---

# 🚀 How to Run the Project

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python app.py
```

### Open in Browser

```
http://127.0.0.1:5000
```

---

# 📊 Expected Output

The application predicts one of the following outcomes based on the entered applicant details:

- ✅ Loan Approved
- ❌ Loan Rejected

The prediction is generated using the trained Random Forest machine learning model.

---

# 🔮 Future Enhancements

- User Authentication
- Database Integration
- Cloud Deployment
- Explainable AI
- Loan History Management
- Responsive Mobile Interface

---

# 👥 Project Team

### Team Leader

- Harshitha Reddy

### Team Members

- Janardhan Kaavali
- Thommandru Kirananjali
- Muni Mohan Krishna Krishna Reddy
- Hepseba Bezawada

---

# 🎓 Academic Information

**Department:** Electrical and Electronics Engineering

**College:** Sri Venkateswara College of Engineering

**Academic Year:** 2026–2027

---

# 📄 License

This project has been developed for academic and educational purposes only.
