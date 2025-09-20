import streamlit as st
from utils.calculations import calculate_scenario, calculate_runway
from utils.report_generator import generate_pdf_report_bytes
from utils.chart_utils import plot_scenario_comparison
from config import bill_flexprice

st.set_page_config(layout="wide")
st.title("CFO Helper Agent - Demo Version")

# Initialize session state
if "scenarios" not in st.session_state:
    st.session_state.scenarios = []
if "usage_count" not in st.session_state:
    st.session_state.usage_count = 0

st.header("Adjust Your Financial Parameters")

# User Inputs
cash = st.number_input("Cash in Hand (₹)", value=1000000, step=50000)
revenue = st.number_input("Monthly Revenue (₹)", value=500000, step=10000)
expenses = st.number_input("Monthly Expenses (₹)", value=300000, step=5000)
marketing = st.slider("Marketing Spend (₹)", 0, 100000, 20000, step=5000)
hiring_cost = st.slider("Hiring Cost (₹)", 0, 200000, 50000, step=10000)
price_increase = st.slider("Product Price Increase (%)", 0, 50, 0, step=5)

# Calculate scenario
adjusted_revenue, total_expenses, profit = calculate_scenario(
    revenue, expenses, marketing, hiring_cost, price_increase
)
runway = calculate_runway(cash, total_expenses, adjusted_revenue)

# Display metrics
st.header("Scenario Outcome")
st.metric("Adjusted Revenue (₹)", f"{adjusted_revenue:,.0f}")
st.metric("Total Expenses (₹)", f"{total_expenses:,.0f}")
st.metric("Profit (₹)", f"{profit:,.0f}")
st.metric("Estimated Runway (months)", f"{runway:,.1f}")

# Save scenario
if st.button("Add Scenario"):
    scenario = {
        "Revenue": adjusted_revenue,
        "Expenses": total_expenses,
        "Profit": profit,
        "Marketing": marketing,
        "Hiring": hiring_cost,
        "Price Increase (%)": price_increase,
        "Runway": runway
    }
    st.session_state.scenarios.append(scenario)
    bill_flexprice("scenario", st)
    st.success("Scenario added and billed!")

# Show usage
st.write(f"Total scenarios tested / billed: {st.session_state.usage_count}")

# Display scenarios & chart
if st.session_state.scenarios:
    plot_scenario_comparison(st.session_state.scenarios)


if st.button("Generate PDF Report"):
    pdf_bytes = generate_pdf_report_bytes(st.session_state.scenarios)
    st.download_button(
        label="Download CFO Helper Report PDF",
        data=pdf_bytes,
        file_name="cfo_helper_report.pdf",
        mime="application/pdf"
    )