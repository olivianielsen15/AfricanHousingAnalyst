# African Housing Analyst

AI-powered chatbot that helps investors, policymakers, and practitioners understand housing issues across Africa and develop appropriate solutions.

## Features

- **Country Housing Profiles** — Get detailed housing market analysis for any African country, powered by live World Bank data and CAHF housing finance indicators
- **Policy Recommendations** — Evidence-based housing policy guidance tailored to specific country contexts
- **Investment Analysis** — Understand housing market opportunities, risks, and return profiles across African markets
- **Market Comparisons** — Compare housing finance depth, affordability, and delivery systems across countries
- **Construction Guidance** — Learn about cost-effective building technologies and materials for the African context

## Data Sources

- **CAHF (Centre for Affordable Housing Finance in Africa)** — Housing finance indicators, affordability benchmarks, country profiles from the annual Housing Finance in Africa Yearbook
- **World Bank (live API)** — GDP, population, urbanization, poverty, infrastructure access, financial depth, and more
- **Expert Knowledge** — Best practices from housing programs across Africa and other developing regions

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/olivianielsen15/AfricanHousingAnalyst.git
   cd AfricanHousingAnalyst
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Get an Anthropic API key from [console.anthropic.com](https://console.anthropic.com)

4. Run the app:
   ```bash
   streamlit run app.py
   ```

5. Enter your API key in the sidebar and start asking questions.

## Example Questions

- "What is the housing situation in Nigeria and what are the key challenges?"
- "Compare mortgage market depth across East African countries"
- "What are the best affordable housing policies for a country with high urbanization?"
- "How can investors assess housing market opportunities in Ghana?"
- "What construction technologies can reduce housing costs in Africa?"

## Architecture

| File | Purpose |
|------|---------|
| `app.py` | Streamlit chat interface |
| `llm.py` | Claude API integration and country detection |
| `world_bank.py` | Live World Bank API client (22 indicators, 54 countries) |
| `knowledge_base.py` | CAHF data, expert knowledge, and system prompt |
