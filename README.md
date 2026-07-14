# 🏦 Smart Lender – Loan Eligibility Prediction Using Machine Learning

A Machine Learning-powered web application that predicts whether a loan applicant is eligible for loan approval based on demographic and financial details. The application uses a trained **Random Forest Classifier** integrated with a **Flask** web application to provide fast and reliable loan eligibility predictions through a clean and user-friendly interface.

---

# 📖 Project Overview

Financial institutions process thousands of loan applications every year. Manual verification is often time-consuming and may lead to inconsistent decisions. Smart Lender automates the preliminary loan screening process using Machine Learning, helping users instantly determine the likelihood of loan approval.

The project demonstrates the complete Machine Learning lifecycle, including:

- Data Collection
- Data Preprocessing
- Exploratory Data Analysis
- Model Training
- Model Evaluation
- Model Deployment using Flask

---

# 🎯 Objectives

- Predict loan eligibility using Machine Learning.
- Reduce manual effort in loan screening.
- Improve prediction accuracy through data-driven analysis.
- Provide a simple and responsive web interface.
- Deploy the trained model for real-time predictions.

---

# ✨ Key Features

- Loan applicant information processing
- Missing value handling
- Categorical feature encoding
- Exploratory Data Analysis (EDA)
- Multiple Machine Learning model comparison
- Best model selection
- Real-time loan eligibility prediction
- Flask-based web application
- Responsive and user-friendly interface

---

# 🛠 Technology Stack

## Programming Language
- Python

## Machine Learning Libraries
- Pandas
- NumPy
- Scikit-learn
- Pickle

## Visualization Libraries
- Matplotlib
- Seaborn

## Web Technologies
- Flask
- HTML5
- CSS3

## Development Tools
- Google Colab
- Visual Studio Code
- GitHub

---

# 🤖 Machine Learning Models

The following Machine Learning algorithms were trained and evaluated during model development.

| Model | Accuracy |
|--------|-----------|
| Decision Tree | 69.11% |
| Random Forest | 75.61% |
| K-Nearest Neighbors (KNN) | 57.72% |
| XGBoost | 75.61% |

## Final Model

**Random Forest Classifier**

Random Forest was selected as the final deployment model because it provided the best balance of prediction accuracy and generalization performance.

The trained model is stored as:

```
loan_model.pkl
```

---

# 🔄 Project Workflow

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
Model Serialization (Pickle)
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
│   │          └── loan-illustration.png
│   │
│   └── templates
│         ├── home.html
│         ├── index.html
│         └── result.html
│
└── README.md
```

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/harshzxx/SmartLender-Loan-Prediction.git
```

---

## Navigate to Project Folder

```bash
cd SmartLender-Loan-Prediction/Flask
```

---

## Install Required Libraries

```bash
pip install -r requirements.txt
```

---

## Run Flask Application

```bash
python app.py
```

---

## Open in Browser

```
http://127.0.0.1:5000
```

---

# 📸 Application Screenshots

## 🏠 Home Page

<img width="1533" height="693" alt="Screenshot 2026-07-13 234720" src="https://github.com/user-attachments/assets/654d676d-e082-47e3-ba47-e01f0d9b8bc2" />


---

## 📝 Loan Prediction Form

<img width="1536" height="732" alt="Screenshot 2026-07-13 234811" src="https://github.com/user-attachments/assets/101d2621-33e0-4fe3-ab79-d8dee20025cc" />


---

## ✅ Loan Approved Result

<img width="1528" height="696" alt="Screenshot 2026-07-13 234633" src="https://github.com/user-attachments/assets/88320cf3-269f-41c9-b000-bd51be99780b" />


---

## ❌ Loan Rejected Result

<img width="1527" height="697" alt="Screenshot 2026-07-13 234704" src="https://github.com/user-attachments/assets/2f0d9a1c-9e83-4271-96ae-4b05440db1e3" />


---

# 📋 Functional Modules

- Dataset Loading
- Data Cleaning
- Missing Value Handling
- Feature Encoding
- Exploratory Data Analysis
- Model Training
- Model Evaluation
- Random Forest Model Selection
- Loan Eligibility Prediction
- Flask Application Deployment

---

# 📈 Future Enhancements

- User Authentication
- Database Integration
- Cloud Deployment
- Prediction History
- Explainable AI (XAI)
- REST API Support
- Mobile-Friendly Interface

---

# 👥 Project Team

**Team Leader**

Harshitha Reddy

**Team Members**

- Janardhan Kaavali
- Thommandru Kirananjali
- Muni Mohan Krishna Krishna Reddy
- Hepseba Bezawada

---

# 🎓 Academic Information

**Project Title**

Smart Lender – Loan Eligibility Prediction Using Machine Learning

**Department**

Electrical and Electronics Engineering

**College**

Sri Venkateswara College of Engineering

**Academic Year**

2026–2027

---

# 📄 License

This project has been developed solely for academic and educational purposes. It is intended for learning, demonstration, and research activities.

---

# ⭐ Acknowledgement

We sincerely thank our faculty members and Sri Venkateswara College of Engineering for their continuous guidance and support throughout the development of this project. Their encouragement and valuable suggestions helped us successfully complete the Smart Lender application.
