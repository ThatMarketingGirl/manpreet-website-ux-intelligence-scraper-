def generate_figma_wireframe(ux_data, visual_data):
    wireframe = {
        "frame": {
            "name": "Landing Page",
            "type": "desktop",
            "width": 1440,
            "height": "auto"
        },

        "layout_system": {
            "grid": "12-column",
            "spacing": "8pt system",
            "alignment": "center + full width sections"
        },

        "components": [
            {
                "section": "Hero",
                "elements": [
                    "Headline (H1)",
                    "Subheading",
                    "Primary CTA Button",
                    "Background visual layer"
                ]
            },
            {
                "section": "Features",
                "elements": [
                    "3–4 feature cards",
                    "Icon + title + description"
                ]
            },
            {
                "section": "Social Proof",
                "elements": [
                    "Testimonials",
                    "Logos row"
                ]
            },
            {
                "section": "Conversion",
                "elements": [
                    "Final CTA block",
                    "Minimal text focus"
                ]
            }
        ],

        "interaction_notes": ux_data.get("motion", "scroll-based transitions inferred"),

        "visual_notes": visual_data.get("visual_hierarchy", "")
    }

    return wireframe
