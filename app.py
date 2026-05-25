import streamlit as st
from datetime import datetime, timezone

st.set_page_config(page_title="Watch Accuracy")

st.title("⌚ Watch Accuracy Tracker")

utc_now = datetime.now(timezone.utc)

st.metric(
    "UTC actual",
    utc_now.strftime("%H:%M:%S")
)

if st.button("REGISTRAR AHORA"):
    st.session_state["captured"] = datetime.now(
        timezone.utc
    ).isoformat()

if "captured" in st.session_state:

    st.success("UTC capturado")

    st.code(st.session_state["captured"])
