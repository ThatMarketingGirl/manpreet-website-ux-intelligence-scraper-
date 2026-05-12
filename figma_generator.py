def generate_figma_wireframe(_, visual_data):

    return {
        "frame": "Desktop 1440px",
        "grid": "12 column system",
        "layout_style": visual_data.get("layout_type"),

        "sections": [
            {
                "name": "Hero",
                "components": ["Heading", "Subheading", "CTA Button", "Visual background"]
            },
            {
                "name": "Features",
                "components": ["3–4 cards", "Icons", "Descriptions"]
            },
            {
                "name": "Social Proof",
                "components": ["Testimonials", "Logos"]
            },
            {
                "name": "CTA Section",
                "components": ["Final conversion block"]
            }
        ],

        "notes": "This is a structural wireframe, not a visual clone."
    }
