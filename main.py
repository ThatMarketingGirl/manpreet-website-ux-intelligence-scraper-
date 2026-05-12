from analyzer import analyze_website
import sys

def ask_questions():
    print("\nAnswer a few questions before analysis:\n")

    goal = input("What are you building from this inspiration? ")
    style = input("Style (minimal, premium, bold, playful): ")
    focus = input("Focus (UX, visuals, conversion, motion): ")
    ignore = input("What should be ignored? ")

    return {
        "goal": goal,
        "style": style,
        "focus": focus,
        "ignore": ignore
    }

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <url>")
        return

    url = sys.argv[1]
    context = ask_questions()

    result = analyze_website(url, context)

    print("\n================ UX REPORT ================\n")
    print(result["ux_report"])

    print("\n================ VISUAL DATA ================\n")
    print(result["visual_data"])

    print("\n================ FIGMA WIREFRAME ================\n")
    print(result["figma_wireframe"])

if __name__ == "__main__":
    main()
