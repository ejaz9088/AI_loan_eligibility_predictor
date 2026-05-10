# 🏦 VIT Bank — AI Loan Eligibility Predictor

A terminal-based AI-powered loan eligibility system built using Python and Machine Learning (Decision Tree Classifier). Developed as a project for **Fundamentals of AI and ML** subject in BTech 1st Year.

---

## 📌 About the Project

VIT Bank Loan Predictor is a software that simulates how a real bank decides whether to approve or reject a customer's loan application. The system uses a **Decision Tree machine learning model** trained on 5000 generated loan records to make predictions based on the applicant's financial profile.

---

## ✨ Features

- ✅ AI-powered loan eligibility prediction
- ✅ Auto-approval for high income (above Rs 3,00,000/month)
- ✅ Auto-approval for high asset value (Rs 1 Crore or above)
- ✅ Loan limit capped at Rs 1,00,00,000 (1 Crore)
- ✅ Personalised rejection tips for the applicant
- ✅ EMI Calculator with full breakdown
- ✅ Terms and Conditions section
- ✅ Input validation (negative values, out-of-range, data errors)
- ✅ Runs completely in the terminal — no UI required

---

## 🤖 AI and ML Concepts Used

| Concept | Description |
|---|---|
| Decision Tree Classifier | Main ML model used to predict loan approval |
| Supervised Learning | Model trained on labelled dataset (approved/rejected) |
| Feature Engineering | Selected 6 key financial features for prediction |
| Risk Scoring | Rule-based logic used to generate training labels |

---

## 📂 Project Files

```
📦 project/
 ┣ 📄 AI_loan_eligibility_predictor.py   → Main application (run this)
 ┣ 📄 loan_data (1).csv            → Auto-generated training dataset
 ┣ 📄 README.md                → This file
 ┗ 📄 Group_Project_Report.pdf        → Detailed project report
```

---

## ⚙️ How to Run

### Step 1 — Install required library
```
pip install scikit-learn pandas
```

### Step 2 — Run the program
```
python AI_loan_eligibility_predictor.py
```

### Step 3 — Use the menu
```
1. Check Loan Eligibility
2. Terms and Conditions
3. EMI Calculator
0. Exit
```

> We recommend reading Terms and Conditions (Option 2) before applying.

---

## 📊 Features Used for Prediction

| Feature | Description |
|---|---|
| Monthly Income | Applicant's monthly salary in Rs |
| Credit Score | CIBIL score between 300 and 900 |
| Loan Amount | Requested loan amount (max Rs 1 Crore) |
| Job Experience | Years of work experience |
| Assets Value | Total value of applicant's assets |
| Existing Loan Dues | Outstanding amount of current loans |

---

## 🏦 Loan Approval Rules

| Condition | Result |
|---|---|
| Monthly income > Rs 3,00,000 | Auto Approved ✅ |
| Total assets ≥ Rs 1,00,00,000 | Auto Approved ✅ |
| Loan amount > Rs 1,00,00,000 | Rejected — exceeds limit ❌ |
| Monthly income < Rs 30,000 | Not eligible ❌ |
| All other cases | Decided by ML model |

---

## 🧠 How the ML Model Works

1. **Dataset is generated** with 5000 realistic records
2. A **risk score** is calculated for each record based on real banking rules
3. Records with risk score ≥ 6 are labelled **Rejected (0)**, others **Approved (1)**
4. A **Decision Tree** learns patterns from this data
5. When a user enters their details, the model **predicts** the outcome

---

## 📋 Requirements

- Python 3.x
- pandas
- scikit-learn

---

## 👨‍💻 Author

Md Ejaz Uddin (25BAI11103), 
Aanjneya Singh (25BAI10885), 
Priyanshi Prajapati (25BAI10054), 
Shivangi Barthwal (25BAI11395), 

BTech 1st Year, 
Subject: Fundamentals of AI and ML


