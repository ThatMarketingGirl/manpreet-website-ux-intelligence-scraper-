from visual_engine import analyze_visual_structure
from figma_generator import generate_figma_wireframe

def analyze_website(url, context):
    visual_data = analyze_visual_structure(url)

    ux_text = f"""
UX INTELLIGENCE REPORT

GOAL:
{context['goal']}

STYLE:
{context['style']}

----------------------

VISUAL ANALYSIS:
{visual_data}

----------------------

UX INSIGHTS:
- Scroll-based structure inferred
- Modular section layout
- Conversion-driven hierarchy

MOTION:
- Likely scroll animations
- Hover micro-interactions
- Soft transitions

DESIGN SYSTEM:
- Grid-based layout (12 column)
- High spacing system
- CTA-driven structure

INSPIRATION NOTES:
- Rebuild structure, not visuals
- Use modular design thinking
"""

    wireframe = generate_figma_wireframe({}, visual_data)

    return {
        "ux_report": ux_text,
        "figma_wireframe": wireframe
    }
