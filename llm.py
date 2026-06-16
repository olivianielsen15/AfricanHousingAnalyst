import re
import anthropic
from world_bank import fetch_and_format, AFRICAN_COUNTRIES, resolve_country_code
from knowledge_base import SYSTEM_PROMPT


def detect_countries(text: str) -> list[str]:
    found = []
    found_codes = set()
    text_lower = text.lower()
    for name in sorted(AFRICAN_COUNTRIES.keys(), key=len, reverse=True):
        pattern = r'\b' + re.escape(name.lower()) + r'\b'
        if re.search(pattern, text_lower):
            code = resolve_country_code(name)
            if code and code not in found_codes:
                found.append(name)
                found_codes.add(code)
    return found[:3]


def build_context(user_message: str) -> str:
    countries = detect_countries(user_message)
    if not countries:
        return ""

    context_parts = []
    for country in countries:
        data = fetch_and_format(country)
        if data:
            context_parts.append(data)

    if context_parts:
        return (
            "\n\n---\n**Live World Bank data retrieved for this query:**\n\n"
            + "\n\n".join(context_parts)
            + "\n\nUse this data to inform your response. Cite specific figures where relevant.\n---\n"
        )
    return ""


def get_response(messages: list[dict], api_key: str) -> str:
    client = anthropic.Anthropic(api_key=api_key)

    last_user_msg = ""
    for msg in reversed(messages):
        if msg["role"] == "user":
            last_user_msg = msg["content"]
            break

    wb_context = build_context(last_user_msg)

    api_messages = []
    for msg in messages:
        if msg["role"] == "user" and msg["content"] == last_user_msg and wb_context:
            api_messages.append({
                "role": "user",
                "content": msg["content"] + wb_context,
            })
        else:
            api_messages.append({"role": msg["role"], "content": msg["content"]})

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=4096,
        system=SYSTEM_PROMPT,
        messages=api_messages,
    )
    return response.content[0].text
