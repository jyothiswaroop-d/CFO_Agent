def bill_flexprice(event_type, st):
    """
    Mock Flexprice billing.
    """
    st.session_state.usage_count += 1
    st.info(f"Mock Flexprice billing triggered for: {event_type}")
