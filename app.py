import streamlit as st
from llm import get_response
from knowledge_base import SAMPLE_QUESTIONS

st.set_page_config(
    page_title="African Housing Analyst",
    page_icon="\U0001f3e0",
    layout="wide",
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .main-header {
        font-size: 2.4rem;
        font-weight: 700;
        color: #1a5632;
        margin-bottom: 0;
        line-height: 1.2;
    }
    .sub-header {
        font-size: 1.15rem;
        color: #555;
        margin-top: 0.25rem;
        margin-bottom: 1.5rem;
    }

    .hero-section {
        background: linear-gradient(135deg, #f0f7f2 0%, #e8f5e9 50%, #fff8e1 100%);
        border-radius: 16px;
        padding: 2rem 2rem 1.5rem 2rem;
        margin-bottom: 1.5rem;
        border: 1px solid #c8e6c9;
    }
    .hero-title {
        font-size: 2.4rem;
        font-weight: 700;
        color: #1a5632;
        margin-bottom: 0.25rem;
    }
    .hero-subtitle {
        font-size: 1.15rem;
        color: #555;
        margin-bottom: 1rem;
    }
    .hero-desc {
        font-size: 0.95rem;
        color: #666;
        line-height: 1.6;
    }

    .audience-card {
        background: white;
        border-radius: 12px;
        padding: 1.25rem;
        border: 1px solid #e0e0e0;
        height: 100%;
    }
    .audience-card h4 {
        color: #1a5632;
        margin-top: 0;
        margin-bottom: 0.5rem;
    }
    .audience-card p {
        color: #666;
        font-size: 0.9rem;
        margin: 0;
        line-height: 1.5;
    }

    .data-badge {
        display: inline-block;
        background: #e8f5e9;
        color: #2e7d32;
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 500;
        margin-right: 0.5rem;
        margin-bottom: 0.5rem;
    }

    .sidebar-section {
        background: #f8f9fa;
        border-radius: 10px;
        padding: 1rem;
        margin-bottom: 1rem;
    }

    div[data-testid="stChatMessage"] {
        border-radius: 12px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def get_api_key() -> str:
    try:
        return st.secrets["ANTHROPIC_API_KEY"]
    except (KeyError, FileNotFoundError):
        return ""


api_key = get_api_key()

with st.sidebar:
    st.markdown(
        """
        <div style="text-align: center; padding: 0.5rem 0 1rem 0;">
            <span style="font-size: 2.5rem;">\U0001f3e0</span>
            <h2 style="color: #1a5632; margin: 0.25rem 0 0 0;">African Housing<br>Analyst</h2>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.divider()

    st.markdown(
        """
        <div class="sidebar-section">
        <h4 style="margin-top:0; color: #1a5632;">\U0001f4ca Data Sources</h4>

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
        <h4 style="margin-top:0; color: #1a5632;">\U0001f30d Coverage</h4>

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
        <div style="text-align: center; padding-top: 1rem;">
            <p style="font-size: 0.75rem; color: #999;">
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
    st.markdown(
        """
        <div class="hero-section">
            <div class="hero-title">\U0001f30d African Housing Analyst</div>
            <div class="hero-subtitle">AI-powered insights on housing markets, policy, and investment across Africa</div>
            <div class="hero-desc">
                Ask questions about housing affordability, mortgage markets, construction costs,
                urban development, land tenure, housing policy, and investment opportunities
                across the continent. Backed by CAHF research and live World Bank data.
            </div>
            <div style="margin-top: 1rem;">
                <span class="data-badge">54 Countries</span>
                <span class="data-badge">Live World Bank Data</span>
                <span class="data-badge">CAHF Research</span>
                <span class="data-badge">Policy Best Practices</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("#### Who is this for?")
    cols = st.columns(3)
    with cols[0]:
        st.markdown(
            """
            <div class="audience-card">
                <h4>\U0001f4bc Investors</h4>
                <p>Assess housing market opportunities, understand risks, and compare
                investment potential across African countries and cities.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with cols[1]:
        st.markdown(
            """
            <div class="audience-card">
                <h4>\U0001f3db Policymakers</h4>
                <p>Design evidence-based housing policies, learn from successful programs
                in peer countries, and understand affordability dynamics.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with cols[2]:
        st.markdown(
            """
            <div class="audience-card">
                <h4>\U0001f527 Practitioners</h4>
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
        '<p class="main-header">\U0001f30d African Housing Analyst</p>',
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
