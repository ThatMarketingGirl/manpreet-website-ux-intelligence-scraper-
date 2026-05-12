from playwright.sync_api import sync_playwright
from PIL import Image
import io

def capture_screenshot(url):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1280, "height": 720})
        page.goto(url, timeout=60000)
        screenshot = page.screenshot(full_page=True)
        browser.close()
        return screenshot

def analyze_visual_structure(url):
    image_bytes = capture_screenshot(url)

    image = Image.open(io.BytesIO(image_bytes))

    width, height = image.size

    # Visual heuristics (simplified intelligence layer)
    analysis = {
        "resolution": f"{width}x{height}",
        "layout_type": "likely vertical scroll layout",
        "visual_hierarchy": "hero section dominant, stacked sections below",
        "spacing_pattern": "high whitespace / modular grid inferred",
        "ui_density": "medium to low density",
        "interaction_zones": [
            "top navigation",
            "hero CTA area",
            "mid-scroll feature blocks",
            "bottom conversion section"
        ]
    }

    return analysis
