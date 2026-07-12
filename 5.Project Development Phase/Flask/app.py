from flask import Flask, render_template, request
import pickle
import pandas as pd

# Create Flask application
app = Flask(__name__)

# Load the trained model
with open("loan_model.pkl", "rb") as file:
    model = pickle.load(file)

# Home Page
@app.route("/")
def home():
    return render_template("index.html")

# Prediction
@app.route("/predict", methods=["POST"])
def predict():

    gender = request.form["Gender"]
    married = request.form["Married"]
    dependents = request.form["Dependents"]
    education = request.form["Education"]
    self_employed = request.form["Self_Employed"]
    applicant_income = float(request.form["ApplicantIncome"])
    coapplicant_income = float(request.form["CoapplicantIncome"])
    loan_amount = float(request.form["LoanAmount"])
    loan_amount_term = float(request.form["Loan_Amount_Term"])
    credit_history = float(request.form["Credit_History"])
    property_area = request.form["Property_Area"]

    # Encode categorical values
    gender = 1 if gender == "Male" else 0
    married = 1 if married == "Yes" else 0

    dependents_map = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3+": 3
    }
    dependents = dependents_map[dependents]

    education = 1 if education == "Graduate" else 0
    self_employed = 1 if self_employed == "Yes" else 0

    property_map = {
        "Rural": 0,
        "Semiurban": 1,
        "Urban": 2
    }
    property_area = property_map[property_area]

    # Create input dataframe
    input_data = pd.DataFrame([[
        gender,
        married,
        dependents,
        education,
        self_employed,
        applicant_income,
        coapplicant_income,
        loan_amount,
        loan_amount_term,
        credit_history,
        property_area
    ]], columns=[
        "Gender",
        "Married",
        "Dependents",
        "Education",
        "Self_Employed",
        "ApplicantIncome",
        "CoapplicantIncome",
        "LoanAmount",
        "Loan_Amount_Term",
        "Credit_History",
        "Property_Area"
    ])

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        result = "Loan Approved"
    else:
        result = "Loan Rejected"

    return render_template("result.html", prediction=result)

if __name__ == "__main__":
    app.run(debug=True)