import streamlit as st
from datetime import datetime, timezone
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Watch Accuracy",
    page_icon="⌚",
    layout="centered"
)

st.title("⌚ Watch Accuracy Tracker")

# ----------------------------------
# UTC Clock (JavaScript)
# ----------------------------------

components.html(
    """
    <div style="
        text-align:center;
        font-size:48px;
        font-weight:bold;
        font-family:monospace;
        margin-bottom:20px;
    ">
        UTC
        <div id="utc-clock"></div>
    </div>

    <script>
    function updateClock() {

        const now = new Date();

        const hh = String(
            now.getUTCHours()
        ).padStart(2,'0');

        const mm = String(
            now.getUTCMinutes()
        ).padStart(2,'0');

        const ss = String(
            now.getUTCSeconds()
        ).padStart(2,'0');

        document.getElementById(
            "utc-clock"
        ).innerHTML =
            hh + ":" + mm + ":" + ss;
    }

    updateClock();

    setInterval(
        updateClock,
        200
    );
    </script>
    """,
    height=120
)

st.divider()

# ----------------------------------
# Hora observada del reloj
# ----------------------------------

st.subheader("Hora observada del reloj")

col1, col2, col3 = st.columns(3)

with col1:
    hour = st.number_input(
        "Hora",
        min_value=0,
        max_value=23,
        value=12,
        step=1
    )

with col2:
    minute = st.number_input(
        "Minuto",
        min_value=0,
        max_value=59,
        value=0,
        step=1
    )

with col3:
    second = st.number_input(
        "Segundo",
        min_value=0,
        max_value=59,
        value=0,
        step=1
    )

watch_time = (
    f"{hour:02d}:"
    f"{minute:02d}:"
    f"{second:02d}"
)

st.markdown(
    f"""
    <h1 style='text-align:center;
               font-family:monospace'>
        {watch_time}
    </h1>
    """,
    unsafe_allow_html=True
)

st.divider()

# ----------------------------------
# Captura
# ----------------------------------

if st.button(
    "📸 REGISTRAR",
    use_container_width=True
):

    utc_capture = datetime.now(
        timezone.utc
    )

    st.session_state["last_capture"] = {
        "watch_time": watch_time,
        "utc_capture": utc_capture.isoformat()
    }

# ----------------------------------
# Resultado
# ----------------------------------

if "last_capture" in st.session_state:

    st.success(
        "Registro capturado"
    )

    st.write(
        "Hora reloj:",
        st.session_state[
            "last_capture"
        ]["watch_time"]
    )

    st.write(
        "UTC capturado:",
        st.session_state[
            "last_capture"
        ]["utc_capture"]
    )
