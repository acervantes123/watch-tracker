import streamlit as st
from datetime import datetime, timezone, date
import streamlit.components.v1 as components

# --------------------------------------------------
# Configuración
# --------------------------------------------------

st.set_page_config(
    page_title="Watch Accuracy",
    page_icon="⌚",
    layout="centered"
)

#st.title("Watch Accuracy Tracker")

# --------------------------------------------------
# UTC Clock (fluido con JavaScript)
# --------------------------------------------------

components.html(
    """
    <div style="
        text-align:center;
        font-size:48px;
        font-weight:bold;
        font-family:monospace;
        margin-bottom:10px;
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

# --------------------------------------------------
# Hora observada del reloj
# --------------------------------------------------

st.subheader("Hora observada del reloj")

current_time = datetime.now()

col1, col2, col3 = st.columns(3)

with col1:
    hour = st.selectbox(
        "Hora",
        options=list(range(24)),
        format_func=lambda x: f"{x:02d}",
        index=current_time.hour
    )

with col2:
    minute = st.selectbox(
        "Minuto",
        options=list(range(60)),
        format_func=lambda x: f"{x:02d}",
        index=current_time.minute
    )

with col3:
    second = st.selectbox(
        "Segundo",
        options=list(range(60)),
        format_func=lambda x: f"{x:02d}",
        index=current_time.second
    )

watch_time = (
    f"{hour:02d}:"
    f"{minute:02d}:"
    f"{second:02d}"
)

st.divider()

# --------------------------------------------------
# Fecha
# --------------------------------------------------

measurement_date = st.date_input(
    "Fecha",
    value=date.today()
)

st.divider()

# --------------------------------------------------
# Captura
# --------------------------------------------------

if st.button(
    "REGISTRAR",
    use_container_width=True
):

    utc_capture = datetime.now(
        timezone.utc
    )

    st.session_state["last_capture"] = {
        "measurement_date": str(
            measurement_date
        ),
        "watch_time": watch_time,
        "utc_capture": utc_capture.isoformat()
    }

# --------------------------------------------------
# Resultado
# --------------------------------------------------

if "last_capture" in st.session_state:

    capture = st.session_state[
        "last_capture"
    ]

    st.success(
        "Registro capturado correctamente"
    )

    st.write(
        "Fecha:",
        capture["measurement_date"]
    )

    st.write(
        "Hora del reloj:",
        capture["watch_time"]
    )

    st.write(
        "UTC capturado:",
        capture["utc_capture"]
    )
