import streamlit as st
from llm import get_response
from hero import get_hero_image_path, PAGE_CSS

st.set_page_config(
    page_title="African Housing Analyst",
    page_icon="\U0001f3e0",
    layout="centered",
)

st.markdown(PAGE_CSS, unsafe_allow_html=True)


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

        **CAHF** — Housing finance indicators, affordability benchmarks, and country profiles

        **World Bank** — Live macroeconomic data, housing program research, and policy toolkits

        **Expert Knowledge** — Best practices from housing programs across the continent
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="sidebar-section">
        <h4>\U0001f30d Coverage</h4>

        Housing market data and analysis for all **54 African countries**, including housing finance, PPPs, rent-to-own, subsidies, informal housing, and more.
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
    img_path = get_hero_image_path()
    if img_path:
        st.image(img_path, use_container_width=True)

    st.markdown(
        '<h1 class="hero-title">African Housing Analyst</h1>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<p class="hero-sub">Ask me anything about housing markets, policy, finance &amp; investment across Africa</p>',
        unsafe_allow_html=True,
    )

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Ask me anything about housing in Africa..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

if st.session_state.messages and st.session_state.messages[-1]["role"] == "user":
    if not api_key:
        with st.chat_message("assistant"):
            st.error(
                "No API key configured. The site administrator needs to add the ANTHROPIC_API_KEY in Streamlit Cloud Settings → Secrets."
            )
    elif not api_key.startswith("sk-ant-"):
        with st.chat_message("assistant"):
            st.error(
                "The API key format looks incorrect. It should start with 'sk-ant-'. Please check the Streamlit Cloud Secrets configuration."
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
                    elif "authentication" in error_msg.lower() or "api key" in error_msg.lower() or "invalid x-api-key" in error_msg.lower() or "401" in error_msg:
                        st.error(
                            "The API key is invalid or has been revoked. Please update it in Streamlit Cloud Settings → Secrets."
                        )
                    elif "credit" in error_msg.lower() or "billing" in error_msg.lower() or "402" in error_msg:
                        st.error(
                            "Your Anthropic account has no credits. Please add credits at console.anthropic.com."
                        )
                    elif "not_found" in error_msg.lower() or "model" in error_msg.lower():
                        st.error(
                            "Model configuration error. Please contact the site administrator."
                        )
                    elif "overloaded" in error_msg.lower() or "529" in error_msg:
                        st.warning(
                            "The AI service is temporarily overloaded. Please try again in a moment."
                        )
                    else:
                        st.error(
                            f"Something went wrong ({type(e).__name__}). Please try again or start a new conversation."
                        )
                    import logging
                    logging.error(f"API error: {error_msg}")
