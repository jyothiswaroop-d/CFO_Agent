import plotly.graph_objects as go
import streamlit as st

def plot_scenario_comparison(scenarios):
    st.header("Scenario Comparison")
    fig = go.Figure()
    for i, sc in enumerate(scenarios, start=1):
        fig.add_trace(go.Bar(name=f"Scenario {i}", x=["Revenue"], y=[sc["Revenue"]]))
        fig.add_trace(go.Bar(name=f"Scenario {i}", x=["Expenses"], y=[sc["Expenses"]]))
        fig.add_trace(go.Bar(name=f"Scenario {i}", x=["Profit"], y=[sc["Profit"]]))
    fig.update_layout(barmode='group', title="Revenue, Expenses, Profit Across Scenarios")
    st.plotly_chart(fig)

    # Show details
    for i, sc in enumerate(scenarios, start=1):
        st.subheader(f"Scenario {i}")
        st.write(sc)
