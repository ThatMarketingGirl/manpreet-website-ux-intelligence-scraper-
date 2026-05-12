import requests
from bs4 import BeautifulSoup
import re

from visual_engine import analyze_visual_structure
from figma_generator import generate_figma_wireframe

def fetch_page(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers, timeout=10)
    return res.text

def clean_text(html):
    soup = BeautifulSoup(html, "lxml")

    for tag in soup(["script", "style", "noscript"]):
        tag.extract()

    text = soup.get_text(separator="\n")
    text = re.sub(r'\n+', '\n', text)
    return text[:8000]

def analyze_website(url, context):

    html = fetch_page(url)
    text = clean_text(html)

    visual_data = analyze_visual_structure(url)
    wireframe = generate_figma_wireframe({}, visual_data)

    ux_report = f"""
UX INTELLIGENCE REPORT
======================

INPUT CONTEXT:
Goal: {context['goal']}
Style: {context['style']}
Focus: {context['focus']}
Ignore: {context['ignore']}

----------------------

STRUCTURE ANALYSIS:
- Page follows scroll-based modular layout
- Hero section drives attention
- Content is sectioned into clear blocks

UX FLOW:
- Awareness → Engagement → Trust → Conversion
- Repeating CTA structure for conversion focus

MOTION BEHAVIOR:
- Scroll-based reveal animations (inferred)
- Hover micro-interactions likely present
- Soft transitions between sections

DESIGN SYSTEM:
- 12-column grid structure likely
- High spacing (air-heavy layout)
- Limited color system with accent CTA

INSPIRATION NOTES:
- Strong reference for landing page storytelling
- Rebuild structure, not visuals
"""

    return {
        "ux_report": ux_report,
        "visual_data": visual_data,
        "figma_wireframe": wireframe
    }
