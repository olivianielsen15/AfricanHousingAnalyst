import requests
from typing import Optional

BASE_URL = "https://api.worldbank.org/v2"

INDICATORS = {
    "population": "SP.POP.TOTL",
    "population_growth": "SP.POP.GROW",
    "urban_population_pct": "SP.URB.TOTL.IN.ZS",
    "urban_population_growth": "SP.URB.GROW",
    "gdp_per_capita": "NY.GDP.PCAP.CD",
    "gdp_growth": "NY.GDP.MKTP.KD.ZG",
    "gni_per_capita": "NY.GNP.PCAP.CD",
    "inflation": "FP.CPI.TOTL.ZG",
    "interest_rate": "FR.INR.LEND",
    "poverty_ratio": "SI.POV.DDAY",
    "gini_index": "SI.POV.GINI",
    "access_electricity": "EG.ELC.ACCS.ZS",
    "access_water": "SH.H2O.BASW.ZS",
    "access_sanitation": "SH.STA.BASS.ZS",
    "land_area": "AG.LND.TOTL.K2",
    "population_density": "EN.POP.DNST",
    "remittances_pct_gdp": "BX.TRF.PWKR.DT.GD.ZS",
    "fdi_net_inflows": "BX.KLT.DINV.CD.WD",
    "domestic_credit": "FS.AST.PRVT.GD.ZS",
    "construction_value_added": "NV.IND.TOTL.ZS",
    "gross_capital_formation": "NE.GDI.TOTL.ZS",
    "mortgage_depth": "FS.AST.DOMS.GD.ZS",
}

AFRICAN_COUNTRIES = {
    "Algeria": "DZA", "Angola": "AGO", "Benin": "BEN", "Botswana": "BWA",
    "Burkina Faso": "BFA", "Burundi": "BDI", "Cabo Verde": "CPV",
    "Cameroon": "CMR", "Central African Republic": "CAF", "Chad": "TCD",
    "Comoros": "COM", "Congo, Dem. Rep.": "COD", "Congo, Rep.": "COG",
    "Cote d'Ivoire": "CIV", "Djibouti": "DJI", "Egypt": "EGY",
    "Equatorial Guinea": "GNQ", "Eritrea": "ERI", "Eswatini": "SWZ",
    "Ethiopia": "ETH", "Gabon": "GAB", "Gambia": "GMB", "Ghana": "GHA",
    "Guinea": "GIN", "Guinea-Bissau": "GNB", "Kenya": "KEN",
    "Lesotho": "LSO", "Liberia": "LBR", "Libya": "LBY",
    "Madagascar": "MDG", "Malawi": "MWI", "Mali": "MLI",
    "Mauritania": "MRT", "Mauritius": "MUS", "Morocco": "MAR",
    "Mozambique": "MOZ", "Namibia": "NAM", "Niger": "NER",
    "Nigeria": "NGA", "Rwanda": "RWA", "Sao Tome and Principe": "STP",
    "Senegal": "SEN", "Seychelles": "SYC", "Sierra Leone": "SLE",
    "Somalia": "SOM", "South Africa": "ZAF", "South Sudan": "SSD",
    "Sudan": "SDN", "Tanzania": "TZA", "Togo": "TGO", "Tunisia": "TUN",
    "Uganda": "UGA", "Zambia": "ZMB", "Zimbabwe": "ZWE", "DRC": "COD",
    "DR Congo": "COD", "Ivory Coast": "CIV", "Cape Verde": "CPV",
}

INDICATOR_LABELS = {
    "SP.POP.TOTL": "Population",
    "SP.POP.GROW": "Population Growth (%)",
    "SP.URB.TOTL.IN.ZS": "Urban Population (%)",
    "SP.URB.GROW": "Urban Population Growth (%)",
    "NY.GDP.PCAP.CD": "GDP per Capita (USD)",
    "NY.GDP.MKTP.KD.ZG": "GDP Growth (%)",
    "NY.GNP.PCAP.CD": "GNI per Capita (USD)",
    "FP.CPI.TOTL.ZG": "Inflation Rate (%)",
    "FR.INR.LEND": "Lending Interest Rate (%)",
    "SI.POV.DDAY": "Poverty Ratio (% at $2.15/day)",
    "SI.POV.GINI": "Gini Index",
    "EG.ELC.ACCS.ZS": "Access to Electricity (%)",
    "SH.H2O.BASW.ZS": "Access to Basic Water (%)",
    "SH.STA.BASS.ZS": "Access to Basic Sanitation (%)",
    "AG.LND.TOTL.K2": "Land Area (sq km)",
    "EN.POP.DNST": "Population Density (per sq km)",
    "BX.TRF.PWKR.DT.GD.ZS": "Remittances (% of GDP)",
    "BX.KLT.DINV.CD.WD": "FDI Net Inflows (USD)",
    "FS.AST.PRVT.GD.ZS": "Domestic Credit to Private Sector (% of GDP)",
    "NV.IND.TOTL.ZS": "Industry Value Added (% of GDP)",
    "NE.GDI.TOTL.ZS": "Gross Capital Formation (% of GDP)",
    "FS.AST.DOMS.GD.ZS": "Domestic Credit (% of GDP)",
}


def resolve_country_code(country_name: str) -> Optional[str]:
    name = country_name.strip().title()
    if len(country_name.strip()) == 3 and country_name.strip().upper() in AFRICAN_COUNTRIES.values():
        return country_name.strip().upper()
    for k, v in AFRICAN_COUNTRIES.items():
        if k.lower() == country_name.strip().lower():
            return v
    for k, v in AFRICAN_COUNTRIES.items():
        if country_name.strip().lower() in k.lower():
            return v
    return None


def fetch_indicator(country_code: str, indicator_code: str, years: int = 5) -> list[dict]:
    url = f"{BASE_URL}/country/{country_code}/indicator/{indicator_code}"
    params = {"format": "json", "per_page": years, "mrv": years}
    try:
        resp = requests.get(url, params=params, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        if len(data) < 2 or not data[1]:
            return []
        return [
            {"year": item["date"], "value": item["value"]}
            for item in data[1]
            if item["value"] is not None
        ]
    except Exception:
        return []


def fetch_country_profile(country_code: str) -> dict:
    profile = {}
    for key, indicator_code in INDICATORS.items():
        data = fetch_indicator(country_code, indicator_code, years=3)
        if data:
            profile[key] = data
    return profile


def format_profile_for_llm(country_name: str, profile: dict) -> str:
    if not profile:
        return f"No World Bank data found for {country_name}."
    lines = [f"## World Bank Data for {country_name} (most recent available)\n"]
    for key, records in profile.items():
        indicator_code = INDICATORS.get(key, key)
        label = INDICATOR_LABELS.get(indicator_code, key.replace("_", " ").title())
        for r in records:
            val = r["value"]
            if isinstance(val, float):
                if abs(val) >= 1_000_000:
                    val = f"{val:,.0f}"
                else:
                    val = f"{val:.2f}"
            lines.append(f"- **{label}** ({r['year']}): {val}")
    return "\n".join(lines)


def fetch_and_format(country_name: str) -> Optional[str]:
    code = resolve_country_code(country_name)
    if not code:
        return None
    profile = fetch_country_profile(code)
    return format_profile_for_llm(country_name, profile)
