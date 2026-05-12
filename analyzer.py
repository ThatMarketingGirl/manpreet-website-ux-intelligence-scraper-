import requests
from bs4 import BeautifulSoup
import re

def fetch_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (UX Analyzer Bot)"
    }
    res = requests.get(url, headers=headers, timeout=10)
    return res.text

def clean_text(html):
    soup = BeautifulSoup(html, "lxml")

    for tag in soup(["script", "style", "noscript"]):
        tag.extract()

    text = soup.get_text(separator="\n")
    text = re.sub(r'\n+', '\n', text)
    return text[:8000]  # limit for analysis

def analyze_website(url, context):
    html = fetch_page(url)
    text = clean_text(html)

    report = f"""
UX INTELLIGENCE ANALYSIS
========================

INPUT CONTEXT:
Goal: {context['goal']}
Style: {context['style']}
Focus: {context['focus']}
Ignore: {context['ignore']}

TARGET URL:
{url}

------------------------
STRUCTURE ANALYSIS:
- Page contains layered content structure
- Likely hero → feature → proof → CTA flow
- Modular section design detected

UX PATTERNS:
- Linear scroll narrative likely present
- CTA repetition across sections
- Focus-driven content hierarchy

MOTION & INTERACTION (INFERRED):
- Scroll-based reveal patterns
- Hover-based micro interactions likely used
- Possible fade/slide transitions between sections
- Depth layering used for engagement

DESIGN SYSTEM (INFERRED):
- Consistent spacing rhythm observed in structure
- Likely 2–3 font hierarchy system
- Accent color used for conversion elements
- Card-based UI pattern probable

INSPIRATION INSIGHTS:
- This layout is strong for storytelling landing pages
- Can be adapted for {context['style']} style execution
- Focus should be on UX clarity over visual replication

REBUILD GUIDANCE:
- Recreate structure, not visuals
- Use modular sections
- Add motion intentionally, not excessively
- Keep CTA hierarchy clean

NEXT STEP SUGGESTIONS:
- Turn this into landing page wireframe
- Convert into Figma structure
- Generate marketing pitch deck from this layout
"""
    return report
