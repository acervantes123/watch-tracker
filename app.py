import streamlit as st
from streamlit_autorefresh import st_autorefresh
from datetime import datetime, timezone

# -----------------------------
# Configuración
# -----------------------------
st.set_page_config(
    page_title="Watch Accuracy",
    page_icon="⌚",
    layout="centered"
)

# Refrescar cada segundo
st_autorefresh(
    interval=1000,
    key="utc_clock"
)

# -----------------------------
# Título
# -----------------------------
st.title("⌚ Watch Accuracy Tracker")

# -----------------------------
# Hora UTC actual
# -----------------------------
utc_now = datetime.now(timezone.utc)

hh = utc_now.strftime("%H")
mm = utc_now.strftime("%M")
ss = utc_now.strftime("%S")

# Hora principal
st.markdown("## UTC NOW")

st.markdown(
    f"""
    <h1 style='text-align:center;'>
        {hh}:{mm}:{ss}
    </h1>
    """,
    unsafe_allow_html=True
)

# Milisegundos
st.markdown(
    f"""
    <div style='text-align:center;
                font-size:24px;
                font-family:monospace;'>
        {utc_now.strftime("%H:%M:%S.%f")[:-3]}
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# -----------------------------
# HH MM SS separados
# -----------------------------
c1, c2, c3 = st.columns(3)

with c1:
    st.metric("HH", hh)

with c2:
    st.metric("MM", mm)

with c3:
    st.metric("SS", ss)

st.divider()

# -----------------------------
# Captura de referencia
# -----------------------------
if st.button(
    "📸 REGISTRAR AHORA",
    use_container_width=True
):
    st.session_state["captured_utc"] = (
        datetime.now(timezone.utc)
    )

# Mostrar captura congelada
if "captured_utc" in st.session_state:

    captured = st.session_state["captured_utc"]

    st.success("UTC capturado correctamente")

    st.code(
        captured.strftime(
            "%Y-%m-%d %H:%M:%S.%f UTC"
        )[:-3]
    )
