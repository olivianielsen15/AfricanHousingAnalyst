import streamlit as st
from llm import get_response
from knowledge_base import SAMPLE_QUESTIONS
from hero import HERO_HTML, HERO_CSS

st.set_page_config(
    page_title="African Housing Analyst",
    page_icon="\U0001f3e0",
    layout="wide",
)

st.markdown(HERO_CSS, unsafe_allow_html=True)


def get_api_key() -> str:
    try:
        return st.secrets["ANTHROPIC_API_KEY"]
    except (KeyError, FileNotFoundError):
        return ""


api_key = get_api_key()

with st.sidebar:
    st.markdown(
        """
        <div class="sidebar-logo">
            <span style="font-size: 2.5rem;">\U0001f3e0</span>
            <h2>African Housing<br>Analyst</h2>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.divider()

    st.markdown(
        """
        <div class="sidebar-section">
        <h4>\U0001f4ca Data Sources</h4>

        **CAHF** — Housing finance indicators, affordability benchmarks, and country profiles from Africa's leading housing research centre

        **World Bank** — Live macroeconomic data including GDP, urbanization, poverty, and infrastructure metrics

        **Expert Knowledge** — Best practices from housing programs across the continent
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="sidebar-section">
        <h4>\U0001f30d Coverage</h4>

        Housing market data and analysis for all **54 African countries** with deep profiles on key markets including Nigeria, Kenya, South Africa, Ghana, Ethiopia, Morocco, Rwanda, Tanzania, and more.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.divider()

    if st.button("\U0001f504 New Conversation", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.markdown(
        """
        <div class="sidebar-disclaimer">
            <p>
                Powered by AI. Responses are informational and should be
                verified with primary sources for decision-making.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

if "messages" not in st.session_state:
    st.session_state.messages = []

if not st.session_state.messages:
    st.markdown(HERO_HTML, unsafe_allow_html=True)

    st.markdown("")
    st.markdown("#### Who is this for?")
    cols = st.columns(3)
    with cols[0]:
        st.markdown(
            """
            <div class="audience-card-v2">
                <div class="card-icon">\U0001f4bc</div>
                <h4>Investors</h4>
                <p>Assess housing market opportunities, understand risks, and compare
                investment potential across African countries and cities.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with cols[1]:
        st.markdown(
            """
            <div class="audience-card-v2">
                <div class="card-icon">\U0001f3db️</div>
                <h4>Policymakers</h4>
                <p>Design evidence-based housing policies, learn from successful programs
                in peer countries, and understand affordability dynamics.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with cols[2]:
        st.markdown(
            """
            <div class="audience-card-v2">
                <div class="card-icon">\U0001f527</div>
                <h4>Practitioners</h4>
                <p>Get guidance on construction technologies, financing models,
                community engagement, and housing delivery strategies.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("")
    st.markdown("#### Try asking:")
    cols = st.columns(2)
    for i, q in enumerate(SAMPLE_QUESTIONS):
        col = cols[i % 2]
        with col:
            if st.button(q, key=f"sample_{i}", use_container_width=True):
                st.session_state.messages.append({"role": "user", "content": q})
                st.rerun()
else:
    st.markdown(
        '<div class="chat-header">\U0001f30d African Housing Analyst</div>',
        unsafe_allow_html=True,
    )

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Ask about housing in Africa..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

if st.session_state.messages and st.session_state.messages[-1]["role"] == "user":
    if not api_key:
        with st.chat_message("assistant"):
            st.error(
                "This service is temporarily unavailable. Please try again later."
            )
    else:
        with st.chat_message("assistant"):
            with st.spinner("Analyzing housing data..."):
                try:
                    response = get_response(st.session_state.messages, api_key)
                    st.markdown(response)
                    st.session_state.messages.append(
                        {"role": "assistant", "content": response}
                    )
                except Exception as e:
                    error_msg = str(e)
                    if "rate" in error_msg.lower() or "limit" in error_msg.lower():
                        st.warning(
                            "The service is experiencing high demand. Please wait a moment and try again."
                        )
                    else:
                        st.error(
                            "Something went wrong. Please try again or start a new conversation."
                        )
