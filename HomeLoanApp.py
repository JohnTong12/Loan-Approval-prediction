import streamlit as st
import pickle
import pandas as pd
from pydantic import BaseModel, Field
from typing import Literal
import os

# Load the pre-trained pipeline
# Load the pre-trained pipeline
file_path = os.path.join(os.path.dirname(__file__), "models", "pipeline.pkl")
with open(file_path, "rb") as file:
    pipeline = pickle.load(file)

# Pydantic model for input validation
class LoanApplication(BaseModel):
    Gender: Literal["Male", "Female"]
    Married: Literal["Yes", "No"]
    Dependents: Literal["0", "1", "2", "3+"]
    Education: Literal["Graduate", "Not Graduate"]
    Self_Employed: Literal["Yes", "No"]
    Property_Area: Literal["Urban", "Rural", "Semiurban"]
    ApplicantIncome: float = Field(..., ge=150.0, le=81000.0)
    CoapplicantIncome: float = Field(..., ge=0.0, le=41667.0)
    LoanAmount: float = Field(..., ge=9.0, le=700.0)
    Loan_Amount_Term: float = Field(..., ge=12.0, le=480.0)
    Credit_History: float = Field(..., ge=0.0, le=1.0)
    ApplicantIncome_Category: Literal["Low", "Average", "High", "Very High"]
    LoanAmount_bin: Literal["Low", "Average", "High"]

# Prediction function
def predict(loan_data: LoanApplication):
    input_data = pd.DataFrame([loan_data.dict()])
    prediction = pipeline.predict(input_data)
    return "Eligible" if prediction[0] == 1 else "Not Eligible"

def main():
    # Initialize session state for widget keys
    if "reset_trigger" not in st.session_state:
        st.session_state.reset_trigger = 0
    if "reset_financial_trigger" not in st.session_state:
        st.session_state.reset_financial_trigger = 0

    # Streamlit UI
    bg = """<div style='background-color:black; padding:13px'>
            <h1 style='color:white'>🏠 Home Loan Approval Predictor</h1>
            </div>"""
    st.markdown(bg, unsafe_allow_html=True)

    # Personal Information
    st.subheader("Personal Information")
    left, right = st.columns((2, 2))
    Gender = left.selectbox(
        "Gender", ["Male", "Female"], help="Select your gender",
        key=f"gender_{st.session_state.reset_trigger}"
    )
    Married = right.selectbox(
        "Married", ["Yes", "No"], help="Marital status",
        key=f"married_{st.session_state.reset_trigger}"
    )
    Dependents = left.selectbox(
        "Dependents", ["0", "1", "2", "3+"], help="Number of dependents",
        key=f"dependents_{st.session_state.reset_trigger}"
    )
    Education = right.selectbox(
        "Education", ["Graduate", "Not Graduate"], help="Education level",
        key=f"education_{st.session_state.reset_trigger}"
    )
    Self_Employed = left.selectbox(
        "Self Employed", ["No", "Yes"], help="Are you self-employed?",
        key=f"self_employed_{st.session_state.reset_trigger}"
    )
    Property_Area = right.selectbox(
        "Property Area", ["Urban", "Rural", "Semiurban"], help="Location of property",
        key=f"property_area_{st.session_state.reset_trigger}"
    )

    # Financial Information
    st.subheader("Financial Information")
    left, right = st.columns((2, 2))
    ApplicantIncome = left.number_input(
        "Applicant Income",
        min_value=150.0, max_value=81000.0, value=3812.0, step=100.0,
        help="Enter your income (USD). Range: 150 to 81,000. Median: 3,812.",
        key=f"applicant_income_{st.session_state.reset_trigger}_{st.session_state.reset_financial_trigger}"
    )
    CoapplicantIncome = right.number_input(
        "Coapplicant Income",
        min_value=0.0, max_value=41667.0, value=0.0, step=100.0,
        help="Enter co-applicant's income, if any (USD). Range: 0 to 41,667. Often 0.",
        key=f"coapplicant_income_{st.session_state.reset_trigger}_{st.session_state.reset_financial_trigger}"
    )
    LoanAmount = left.number_input(
        "Loan Amount",
        min_value=9.0, max_value=700.0, value=128.0, step=10.0,
        help="Enter loan amount in thousands (e.g., 128 for 128,000 USD). Range: 9 to 700. Median: 128.",
        key=f"loan_amount_{st.session_state.reset_trigger}_{st.session_state.reset_financial_trigger}"
    )
    Loan_Amount_Term = right.number_input(
        "Loan Amount Term",
        min_value=12.0, max_value=480.0, value=360.0, step=12.0,
        help="Loan term in months (e.g., 360 for 30 years). Range: 12 to 480. Common: 360.",
        key=f"loan_amount_term_{st.session_state.reset_trigger}_{st.session_state.reset_financial_trigger}"
    )
    Credit_History = left.number_input(
        "Credit History",
        min_value=0.0, max_value=1.0, value=1.0, step=1.0,
        help="Enter 1 for good credit history, 0 for none/bad.",
        key=f"credit_history_{st.session_state.reset_trigger}_{st.session_state.reset_financial_trigger}"
    )
    ApplicantIncome_Category = right.selectbox(
        "Income Category",
        ["Low", "Average", "High", "Very High"],
        help="Select based on income: Low (≤2,874), Average (2,875–3,812), High (3,813–5,798), Very High (>5,798).",
        key=f"applicant_income_category_{st.session_state.reset_trigger}_{st.session_state.reset_financial_trigger}"
    )
    LoanAmount_bin = left.selectbox(
        "Loan Amount Category",
        ["Low", "Average", "High"],
        help="Select based on loan amount: Low (≤100), Average (101–151), High (>151).",
        key=f"loan_amount_bin_{st.session_state.reset_trigger}_{st.session_state.reset_financial_trigger}"
    )

    # Buttons
    col1, col2, col3 = st.columns(3)
    with col1:
        predict_button = st.button("Predict")
    with col2:
        reset_button = st.button("Reset All")
    with col3:
        reset_financial_button = st.button("Reset Financial")

    # Handle Reset All
    if reset_button:
        st.session_state.reset_trigger += 1
        st.session_state.reset_financial_trigger += 1
        st.success("All fields reset successfully!", icon="🔄")

    # Handle Reset Financial
    if reset_financial_button:
        st.session_state.reset_financial_trigger += 1
        st.success("Financial fields reset successfully!", icon="🔄")

    # Handle Predict
    if predict_button:
        with st.spinner("Predicting..."):
            try:
                loan_data = LoanApplication(
                    Gender=Gender,
                    Married=Married,
                    Dependents=Dependents,
                    Education=Education,
                    Self_Employed=Self_Employed,
                    Property_Area=Property_Area,
                    ApplicantIncome=ApplicantIncome,
                    CoapplicantIncome=CoapplicantIncome,
                    LoanAmount=LoanAmount,
                    Loan_Amount_Term=Loan_Amount_Term,
                    Credit_History=Credit_History,
                    ApplicantIncome_Category=ApplicantIncome_Category,
                    LoanAmount_bin=LoanAmount_bin
                )

                verdict = predict(loan_data)
                if verdict == "Eligible":
                    st.markdown(
                        "<div style='background-color:#d4edda; padding:10px; border-radius:5px;'>"
                        f"<h3 style='color:#155724;'>✅ {verdict}</h3>"
                        "</div>",
                        unsafe_allow_html=True
                    )
                else:
                    st.markdown(
                        "<div style='background-color:#f8d7da; padding:10px; border-radius:5px;'>"
                        f"<h3 style='color:#721c24;'>❌ {verdict}</h3>"
                        "</div>",
                        unsafe_allow_html=True
                    )
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
