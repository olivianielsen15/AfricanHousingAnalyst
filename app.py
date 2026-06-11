import streamlit as st
from llm import get_response
from knowledge_base import SAMPLE_QUESTIONS

st.set_page_config(
    page_title="African Housing Analyst",
    page_icon="🏠",
    layout="wide",
)

st.markdown(
    """
    <style>
    .main-header {
        font-size: 2.2rem;
        font-weight: 700;
        color: #1a5632;
        margin-bottom: 0;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #555;
        margin-top: 0;
        margin-bottom: 1.5rem;
    }
    .stChatMessage {
        border-radius: 12px;
    }
    .sample-btn {
        margin: 2px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

with st.sidebar:
    st.markdown("### Settings")
    api_key = st.text_input(
        "Anthropic API Key",
        type="password",
        help="Get your key at console.anthropic.com",
    )

    st.divider()
    st.markdown("### About")
    st.markdown(
        """
        **African Housing Analyst** helps investors, policymakers, and
        practitioners understand housing markets across Africa.

        **Data sources:**
        - CAHF housing finance data & country profiles
        - World Bank live indicators (population, GDP, urbanization, etc.)
        - Best practices from housing programs across Africa

        **Capabilities:**
        - Country housing profiles & comparisons
        - Policy analysis & recommendations
        - Investment opportunity assessment
        - Construction cost & technology guidance
        """
    )

    st.divider()
    if st.button("Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

st.markdown('<p class="main-header">African Housing Analyst</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="sub-header">AI-powered insights on housing markets, policy, and investment across Africa</p>',
    unsafe_allow_html=True,
)

if "messages" not in st.session_state:
    st.session_state.messages = []

if not st.session_state.messages:
    st.markdown("#### Try asking about:")
    cols = st.columns(2)
    for i, q in enumerate(SAMPLE_QUESTIONS):
        col = cols[i % 2]
        with col:
            if st.button(q, key=f"sample_{i}", use_container_width=True):
                st.session_state.messages.append({"role": "user", "content": q})
                st.rerun()

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
            st.warning("Please enter your Anthropic API key in the sidebar to get started.")
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
                    if "authentication" in error_msg.lower() or "api key" in error_msg.lower():
                        st.error("Invalid API key. Please check your Anthropic API key in the sidebar.")
                    else:
                        st.error(f"An error occurred: {error_msg}")
