# 🏦 Smart Lender – Machine Learning Based Loan Eligibility Prediction

Smart Lender is a Machine Learning-based web application that predicts whether a loan applicant is eligible for loan approval based on personal and financial information. The application uses a trained **Random Forest** model integrated with a **Flask** web application to provide instant loan eligibility predictions through a simple and interactive interface.

---

# 📌 Project Overview

Financial institutions receive numerous loan applications every day, making manual verification time-consuming and prone to inconsistencies. Smart Lender addresses this challenge by analyzing applicant information and predicting loan eligibility using machine learning techniques.

The project covers the complete machine learning workflow, including data preprocessing, exploratory data analysis, model training, model evaluation, and deployment using Flask.

---

# 🎯 Objectives

- Predict loan approval using machine learning.
- Automate the loan eligibility prediction process.
- Improve decision-making through data-driven analysis.
- Provide a user-friendly web interface.
- Deploy the trained model using Flask.

---

# ✨ Features

- Loan applicant data preprocessing
- Missing value handling
- Categorical feature encoding
- Exploratory Data Analysis (EDA)
- Multiple Machine Learning model training
- Model performance comparison
- Real-time loan eligibility prediction
- Flask-based web application
- Interactive prediction results

---

# 🛠 Technology Stack

### Programming Language
- Python

### Machine Learning Libraries
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Pickle

### Web Technologies
- Flask
- HTML5
- CSS3

### Development Tools
- Google Colaboratory
- Visual Studio Code
- GitHub

---

# 🤖 Machine Learning Models

The following models were trained and evaluated:

| Model | Accuracy |
|--------|----------|
| Decision Tree | 69.11% |
| Random Forest | 75.61% |
| K-Nearest Neighbors | 57.72% |
| XGBoost | 75.61% |

### Selected Model

**Random Forest Classifier**

The Random Forest model achieved the best overall performance and was selected for deployment. The trained model is saved as **loan_model.pkl**.

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
Best Model Selection
      │
      ▼
Model Serialization (.pkl)
      │
      ▼
Flask Web Application
      │
      ▼
Loan Eligibility Prediction
```

---

# 📂 Project Structure

```text
Smart_Lender/
│
├── Dataset/
│   └── loan_prediction.csv
│
├── Training/
│   └── SmartLender_Model_Training.ipynb
│
├── Flask/
│   ├── app.py
│   ├── loan_model.pkl
│   ├── requirements.txt
│   │
│   ├── static/
│   │     └── style.css
│   │
│   └── templates/
│         ├── index.html
│         └── result.html
│
└── README.md
```

---

# 🚀 Installation Guide

### Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Smart_Lender.git
```

### Navigate to the Flask Folder

```bash
cd Smart_Lender/Flask
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python app.py
```

### Open the Application

```
http://127.0.0.1:5000
```

---

# 📸 Application Screenshots

## Loan Eligibility Prediction Form

*<img width="1297" height="732" alt="Screenshot 2026-07-12 110438" src="https://github.com/user-attachments/assets/cf9023c9-9f7e-4944-beef-3722da81084a" />
.*

---

## Loan Approval Prediction

*<img width="1020" height="447" alt="Screenshot 2026-07-12 103446" src="https://github.com/user-attachments/assets/791cf8c6-9e74-456e-b8bf-d10a018746d3" />)*

---

## Loan Rejection Prediction

*<img width="991" height="405" alt="Screenshot 2026-07-12 110600" src="https://github.com/user-attachments/assets/485afa9f-04d1-4d49-a7bf-8b7d3813a1ee" />
*

---

# 📋 Functional Modules

- Dataset Import
- Data Cleaning
- Missing Value Handling
- Feature Encoding
- Exploratory Data Analysis
- Model Training
- Model Evaluation
- Loan Eligibility Prediction
- Flask Application Deployment

---

# 🔮 Future Enhancements

- User Authentication
- Database Integration
- Cloud Deployment
- Explainable AI for Prediction Analysis
- Loan Application History
- Responsive Mobile Interface

---

# 👩‍💻 Developer

**Harshitha**

Bachelor of Technology (B.Tech)

Electrical and Electronics Engineering (EEE)

Sri Venkateswara College of Engineering

Academic Year: **2026–2027**

---

# 📜 License

This project has been developed for academic and educational purposes only.
