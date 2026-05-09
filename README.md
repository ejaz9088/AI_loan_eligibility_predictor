# AI_loan_eligibility_predictor

🏦 VIT Bank — AI Loan Eligibility Predictor
A terminal-based AI-powered loan eligibility system built using Python and Machine Learning (Decision Tree Classifier). Developed as a project for Fundamentals of AI and ML subject in BTech 1st Year.

📌 About the Project
VIT Bank Loan Predictor is a software that simulates how a real bank decides whether to approve or reject a customer's loan application. The system uses a Decision Tree machine learning model trained on 3000 generated loan records to make predictions based on the applicant's financial profile.

✨ Features

✅ AI-powered loan eligibility prediction
✅ Auto-approval for high income (above Rs 3,00,000/month)
✅ Auto-approval for high asset value (Rs 1 Crore or above)
✅ Loan limit capped at Rs 1,00,00,000 (1 Crore)
✅ Personalised rejection tips for the applicant
✅ EMI Calculator with full breakdown
✅ Terms and Conditions section
✅ Input validation (negative values, out-of-range, data errors)
✅ Runs completely in the terminal — no UI required


🤖 AI and ML Concepts Used
ConceptDescriptionDecision Tree ClassifierMain ML model used to predict loan approvalSupervised LearningModel trained on labelled dataset (approved/rejected)Feature EngineeringSelected 6 key financial features for predictionRisk ScoringRule-based logic used to generate training labels

📂 Project Files
📦 project/
 ┣ 📄 home_loan_predictor.py   → Main application (run this)
 ┣ 📄 loan_data.csv            → Auto-generated training dataset
 ┣ 📄 README.md                → This file
 ┗ 📄 Project_Report.md        → Detailed project report

⚙️ How to Run
Step 1 — Install required library
pip install scikit-learn pandas
Step 2 — Run the program
python home_loan_predictor.py
Step 3 — Use the menu
1. Check Loan Eligibility
2. Terms and Conditions
3. EMI Calculator
0. Exit

We recommend reading Terms and Conditions (Option 2) before applying.


📊 Features Used for Prediction
FeatureDescriptionMonthly IncomeApplicant's monthly salary in RsCredit ScoreCIBIL score between 300 and 900Loan AmountRequested loan amount (max Rs 1 Crore)Job ExperienceYears of work experienceAssets ValueTotal value of applicant's assetsExisting Loan DuesOutstanding amount of current loans

🏦 Loan Approval Rules
ConditionResultMonthly income > Rs 3,00,000Auto Approved ✅Total assets ≥ Rs 1,00,00,000Auto Approved ✅Loan amount > Rs 1,00,00,000Rejected — exceeds limit ❌Monthly income < Rs 30,000Not eligible ❌All other casesDecided by ML model

🧠 How the ML Model Works

Dataset is generated with 3000 realistic records
A risk score is calculated for each record based on real banking rules
Records with risk score ≥ 6 are labelled Rejected (0), others Approved (1)
A Decision Tree learns patterns from this data
When a user enters their details, the model predicts the outcome


📋 Requirements

Python 3.x
pandas
scikit-learn
