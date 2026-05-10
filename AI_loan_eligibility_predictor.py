import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import warnings
import os
warnings.filterwarnings("ignore")




csv_path = r"C:\Users\uddin\Downloads\loan_data (1).csv"   
                        

df = pd.read_csv(csv_path)
print("Dataset loaded! Total records:", len(df))
print("Approved:", df['approval'].sum(), "| Rejected:", len(df) - df['approval'].sum())



# TRAIN ML MODEL

X = df[['income', 'credit_score', 'loan_amount',
        'job_experience', 'assets_value', 'existing_loan_amount']]
y = df['approval']

model = DecisionTreeClassifier(max_depth=10, random_state=42)
model.fit(X, y)



# INPUT HELPER FUNCTIONS

def get_positive_int(prompt, min_val, max_val):
    while True:
        try:
            val = int(input(prompt))
            if val < 0:
                print("  Error: Value cannot be negative. Please try again.")
            elif val < min_val or val > max_val:
                print("  Please enter a value between", min_val, "and", max_val)
            else:
                return val
        except:
            print("  Invalid input. Please enter a whole number.")


def get_positive_float(prompt):
    while True:
        try:
            val = float(input(prompt))
            if val < 0:
                print("  Error: Value cannot be negative. Please try again.")
            else:
                return val
        except:
            print("  Invalid input. Please enter a number.")



# WELCOME SCREEN

print()
print("=" * 54)
print("            WELCOME TO VIT BANK")
print("        Your Trusted Financial Partner")
print("     Home Loans | Personal Loans | Business")
print("=" * 54)
print()
print("  We are committed to helping you achieve your")
print("  financial goals with transparent and fair")
print("  loan assessment powered by AI.")
print()
print("  ⚠  We advise you to please read our Terms")
print("     and Conditions (Option 2) before applying.")
print()
print("=" * 54)



# MAIN MENU

while True:
    print()
    print("  What would you like to do?")
    print()
    print("  1. Check Loan Eligibility")
    print("  2. Terms and Conditions")
    print("  3. EMI Calculator")
    print("  0. Exit")
    print()

    choice = input("  Enter your choice: ")


    
    # OPTION 1 - LOAN CHECK
    
    if choice == "1":
        print()
        print("=" * 54)
        print("           LOAN ELIGIBILITY CHECK")
        print("=" * 54)
        print()

        # --- Personal Details ---
        name = input("  Full Name                              : ").strip()
        if name == "":
            name = "Applicant"

        print()

        # Job Type (for records only, not used in decision)
        print("  Job Type:")
        print("  1. Salaried - Private Sector")
        print("  2. Salaried - Government / PSU")
        print("  3. Self Employed / Business Owner")
        print("  4. Freelancer / Consultant")
        print("  5. Doctor / Medical Professional")
        print("  6. Lawyer / CA / CS")
        print("  7. Teacher / Professor")
        print("  8. Retired / Pensioner")
        print("  9. Other")
        job_choice = input("  Select (1-9)                           : ").strip()
        job_labels = {
            "1": "Salaried (Private)",
            "2": "Salaried (Government/PSU)",
            "3": "Self Employed / Business",
            "4": "Freelancer / Consultant",
            "5": "Doctor / Medical Professional",
            "6": "Lawyer / CA / CS",
            "7": "Teacher / Professor",
            "8": "Retired / Pensioner",
            "9": "Other"
        }
        job_label = job_labels.get(job_choice, "Other")

        print()

        # Job experience
        while True:
            try:
                job_experience = int(input("  Job Experience (Years)                 : "))
                if job_experience < 0:
                    print("  Error: Value cannot be negative.")
                elif job_experience > 50:
                    print("  Data Error: Job experience cannot exceed 50 years.")
                else:
                    break
            except:
                print("  Invalid input. Please enter a number.")

        print()
        print("  --- Financial Details ---")
        print()

        # Monthly income
        while True:
            try:
                income = int(input("  Monthly Income (Rs)                    : "))
                if income < 0:
                    print("  Error: Value cannot be negative.")
                elif income < 30000:
                    print("  Sorry, minimum monthly income required is Rs 30,000.")
                else:
                    break
            except:
                print("  Invalid input. Please enter a number.")

        # Check salary auto-approve before asking rest
        if income > 300000:
            print()
            print("=" * 54)
            print()
            print("  Dear", name + ",")
            print()
            print("  RESULT: Loan APPROVED ✅")
            print()
            print("  Your monthly income exceeds Rs 3,00,000.")
            print("  You qualify for our premium loan category.")
            print("  Our representative will contact you within")
            print("  2 working days.")
            print()
            print("=" * 54)
            continue

        # Loan amount
        loan_amount_input = input(
            "  Loan Amount Required (Rs)              : ").strip()

        try:
            loan_amount = int(loan_amount_input)
        except:
            print("  Invalid input.")
            continue

        if loan_amount < 0:
            print("  Error: Loan amount cannot be negative.")
            continue

        if loan_amount == 0:
            print("  Error: Loan amount must be greater than 0.")
            continue

        if loan_amount > 10000000:
            print()
            print("  Sorry", name + ",")
            print("  We provide loans up to Rs 1,00,00,000 (1 Crore) only.")
            print("  For higher amounts, please visit our nearest branch.")
            continue

        # Assets value
        assets_value = get_positive_int(
            "  Total Assets Value (Rs)                : ",
            0, 100000000)

        # Auto approve if assets >= 1 crore
        if assets_value >= 10000000:
            print()
            print("=" * 54)
            print()
            print("  Dear", name + ",")
            print()
            print("  RESULT: Loan APPROVED ✅")
            print()
            print("  Your assets value is Rs 1 Crore or above.")
            print("  You qualify for our secured loan category.")
            print("  Our team will contact you within 2 working")
            print("  days to complete the documentation.")
            print()
            print("=" * 54)
            continue

        # Credit score
        credit_score = get_positive_int(
            "  Credit Score (300 - 900)               : ",
            300, 900)

        # Existing loan amount
        existing_loan_amount = get_positive_int(
            "  Total Existing Loan Dues (Rs)          : ",
            0, 10000000)

        # --- ML PREDICTION ---
        user_data = pd.DataFrame([[income, credit_score, loan_amount,
                                   job_experience, assets_value, existing_loan_amount]],
                                 columns=['income', 'credit_score', 'loan_amount',
                                          'job_experience', 'assets_value', 'existing_loan_amount'])

        result = model.predict(user_data)

        print()
        print("=" * 54)
        print()
        print("  Dear", name + ",")
        print("  Profession:", job_label)
        print()

        if result[0] == 1:
            print("  RESULT: Loan APPROVED ✅")
            print()
            print("  Congratulations! Your profile qualifies.")
            print("  Our team will contact you within 3 working")
            print("  days to proceed with the documentation.")
            print()
            print("  Approved loan amount: Rs", "{:,}".format(loan_amount))
        else:
            print("  RESULT: Loan REJECTED ❌")
            print()
            print("  Your profile does not meet our current")
            print("  lending criteria. Here is why:")
            print()

            if credit_score < 650:
                print("  - Credit score is low (below 650)")
                print("    Tip: Pay bills on time to improve it.")
            if loan_amount > income * 60:
                print("  - Loan amount exceeds 60x your monthly income")
                print("    Tip: Apply for a smaller loan amount.")
            if existing_loan_amount > income * 12:
                print("  - High existing loan burden detected")
                print("    Tip: Close some existing loans first.")
            if job_experience < 2:
                print("  - Less than 2 years of work experience")
                print("    Tip: Reapply after gaining more experience.")
            if assets_value < loan_amount * 0.5:
                print("  - Assets value is low vs loan amount")
                print("    Tip: Provide more asset collateral.")

            print()
            print("  You may reapply after 6 months.")

        print()
        print("=" * 54)


    
    # OPTION 2 - TERMS AND CONDITIONS
    
    elif choice == "2":
        print()
        print("=" * 54)
        print("      VIT BANK - TERMS AND CONDITIONS")
        print("=" * 54)
        print()
        print("  LOAN AMOUNT")
        print()
        print("  1. VIT Bank provides loans up to a maximum")
        print("     of Rs 1,00,00,000 (1 Crore) only.")
        print("     For higher loan requirements, visit the")
        print("     nearest branch for special assessment.")
        print()
        print("  INCOME CRITERIA")
        print()
        print("  2. Minimum monthly income required: Rs 30,000")
        print("     Applicants earning below Rs 30,000 per")
        print("     month are not eligible to apply.")
        print()
        print("  3. Applicants with monthly income above")
        print("     Rs 3,00,000 are automatically approved")
        print("     and qualify for our premium loan tier.")
        print()
        print("  ASSET CRITERIA")
        print()
        print("  4. Applicants with total verified assets")
        print("     of Rs 1,00,00,000 (1 Crore) or above")
        print("     are automatically approved for a loan.")
        print()
        print("  CREDIT SCORE")
        print()
        print("  5. A credit score of 750 or above is")
        print("     considered excellent.")
        print("  6. Credit score below 550 significantly")
        print("     reduces chances of loan approval.")
        print("  7. CIBIL score is checked from official")
        print("     credit bureaus during processing.")
        print()
        print("  INTEREST RATES (Indicative)")
        print()
        print("  8. Home Loan         : 8.5% - 10.5% p.a.")
        print("     Personal Loan     : 10.5% - 16% p.a.")
        print("     Business Loan     : 11% - 18% p.a.")
        print("     (Rates vary based on profile and tenure)")
        print()
        print("  LOAN TENURE & FEES")
        print()
        print("  9. Loan repayment period: 1 year to 30 years")
        print(" 10. Processing fee: 0.5% to 1% of loan amount")
        print(" 11. Prepayment penalty: 2% of outstanding")
        print("     amount if closed before 1 year.")
        print()
        print("  GENERAL TERMS")
        print()
        print(" 12. The AI assessment is preliminary only.")
        print("     Final approval is subject to document")
        print("     verification by our loan officers.")
        print(" 13. VIT Bank reserves the right to cancel")
        print("     any application without prior notice.")
        print(" 14. All submitted information is confidential")
        print("     and protected under data privacy laws.")
        print(" 15. Reapplication is allowed only after")
        print("     a minimum gap of 6 months post rejection.")
        print()
        print("=" * 54)


    
    # OPTION 3 - EMI CALCULATOR
    
    elif choice == "3":
        print()
        print("=" * 54)
        print("              EMI CALCULATOR")
        print("=" * 54)
        print()

        try:
            principal = float(input("  Loan Amount (Rs)               : "))
            if principal < 0:
                print("  Error: Amount cannot be negative.")
                continue
            if principal > 10000000:
                print("  Error: We provide loans up to Rs 1 Crore only.")
                continue

            annual_rate = float(input("  Annual Interest Rate (%)        : "))
            if annual_rate < 0:
                print("  Error: Interest rate cannot be negative.")
                continue

            years = int(input("  Loan Duration (in Years, 1-30)  : "))
            if years < 0:
                print("  Error: Duration cannot be negative.")
                continue
            if years < 1 or years > 30:
                print("  Please enter duration between 1 and 30 years.")
                continue

            r   = annual_rate / 12 / 100
            n   = years * 12

            emi            = principal * r * (1 + r) ** n / ((1 + r) ** n - 1)
            total_payment  = emi * n
            total_interest = total_payment - principal

            print()
            print("  --- Your EMI Details ---")
            print()
            print("  Loan Amount         : Rs", "{:,.0f}".format(principal))
            print("  Interest Rate       :", annual_rate, "% per annum")
            print("  Loan Tenure         :", years, "years (", n, "months )")
            print()
            print("  Monthly EMI         : Rs", "{:,.0f}".format(emi))
            print("  Total Amount Payable: Rs", "{:,.0f}".format(total_payment))
            print("  Total Interest Paid : Rs", "{:,.0f}".format(total_interest))

        except:
            print("  Invalid input. Please enter valid numbers.")

        print()
        print("=" * 54)


    
    # EXIT
    
    elif choice == "0":
        print()
        print("  Thank you for choosing VIT Bank!")
        print("  Have a great day. Goodbye!")
        print()
        break

    else:
        print("  Invalid choice. Please enter 1, 2, 3 or 0.")