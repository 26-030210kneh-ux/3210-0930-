import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Brick Breaker",
    page_icon="🧱",
    layout="centered"
)

BASE_DIR = Path(__file__).parent
GAME_FILE = BASE_DIR / "game.html"

game_html = GAME_FILE.read_text(encoding="utf-8")

st.markdown(
    """
    <style>
        .block-container {
            max-width: 850px;
            padding-top: 1rem;
            padding-bottom: 1rem;
        }

        header {
            visibility: hidden;
        }

        iframe {
            border: none !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🧱 Brick Breaker")
st.caption("벽돌을 모두 깨고 최고 점수에 도전하세요!")

st.components.v1.html(
    game_html,
    height=760,
    scrolling=False
)
