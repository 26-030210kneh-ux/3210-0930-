import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="🧱 Brick Breaker",
    page_icon="🧱",
    layout="centered",
)

html_path = Path(__file__).parent / "game.html"
game_html = html_path.read_text(encoding="utf-8")

st.markdown(
    """
    <style>
        .block-container {
            padding-top: 1rem;
            padding-bottom: 1rem;
            max-width: 850px;
        }

        header {
            visibility: hidden;
        }

        iframe {
            border: none !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🧱 Brick Breaker")
st.caption("벽돌을 모두 깨고 최고 점수에 도전하세요!")

st.components.v1.html(
    game_html,
    height=720,
    scrolling=False,
)
