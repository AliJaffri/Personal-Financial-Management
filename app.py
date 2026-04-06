import streamlit as st
    if surplus < 0:
        advice.append("You are spending more than your monthly income. The first goal should be to reduce non-essential expenses.")
    else:
        advice.append("You have a positive monthly surplus. That is a strong starting point for saving and investing.")

    if savings_rate < 0.10:
        advice.append("Your savings rate is below 10%. Try increasing savings gradually by reducing discretionary spending.")
    elif savings_rate < 0.20:
        advice.append("Your savings rate is reasonable, but there is room to improve if you want to build wealth faster.")
    else:
        advice.append("Your savings rate is strong. This gives you more flexibility for investing and emergency planning.")

    if debt_to_income > 0.35:
        advice.append("Your debt burden is high relative to income. You should prioritize debt reduction before taking on more obligations.")
    elif debt_to_income > 0.20:
        advice.append("Your debt level is manageable, but keeping it under control should remain a priority.")
    else:
        advice.append("Your debt payment level appears healthy relative to income.")

    if housing_ratio > 0.30:
        advice.append("Your housing cost is more than 30% of income, which may place pressure on your budget.")
    else:
        advice.append("Your housing cost is within a commonly used affordability range.")

    if current_savings < emergency_fund_target:
        advice.append("Build your emergency fund toward at least 6 months of essential expenses.")
    else:
        advice.append("Your emergency savings position looks solid based on this simple benchmark.")

    for i, item in enumerate(advice, start=1):
        st.write(f"{i}. {item}")

    # -----------------------------
    # BASIC FINANCIAL HEALTH SCORE
    # -----------------------------
    score = 0

    if surplus > 0:
        score += 25
    if savings_rate >= 0.20:
        score += 25
    elif savings_rate >= 0.10:
        score += 15

    if debt_to_income <= 0.20:
        score += 25
    elif debt_to_income <= 0.35:
        score += 15

    if current_savings >= emergency_fund_target:
        score += 25
    elif current_savings >= emergency_fund_target / 2:
        score += 15

    st.subheader("Financial Health Score")
    st.write(f"Score: {score}/100")

    if score >= 80:
        st.success("Your financial position looks strong based on these simple rules.")
    elif score >= 50:
        st.info("Your financial position is moderate, with room for improvement.")
    else:
        st.error("Your financial position needs attention, especially budgeting, debt control, or savings growth.")
