import streamlit as st

st.title("Personal Financial Advisory App")

# Inputs
monthly_income = st.number_input("Monthly Income", value=4000.0)
expenses = st.number_input("Total Monthly Expenses", value=3000.0)
debt_payment = st.number_input("Monthly Debt Payment", value=500.0)

# Button
if st.button("Analyze"):

    # Calculations
    surplus = monthly_income - expenses

    if monthly_income > 0:
        savings_rate = max(surplus, 0) / monthly_income
        debt_to_income = debt_payment / monthly_income
    else:
        savings_rate = 0
        debt_to_income = 0

    # Output
    st.write(f"Surplus: ${surplus:.2f}")
    st.write(f"Savings Rate: {savings_rate:.2%}")
    st.write(f"Debt-to-Income: {debt_to_income:.2%}")

    # Advice (THIS is where your error was)
    if surplus < 0:
        st.error("You are spending more than your income.")
    else:
        st.success("You have a positive surplus.")

    if savings_rate < 0.1:
        st.warning("Low savings rate.")
    else:
        st.success("Good savings rate.")

    if debt_to_income > 0.3:
        st.warning("High debt burden.")
    else:
        st.success("Debt level is manageable.")
