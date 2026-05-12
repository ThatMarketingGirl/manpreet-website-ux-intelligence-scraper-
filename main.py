import sys
from analyzer import analyze_website

def ask_questions():
    print("\nBefore analyzing, answer a few questions:\n")

    goal = input("What are you building from this inspiration? ")
    style = input("Desired style (minimal, premium, bold, playful, etc): ")
    focus = input("What matters most (UX, visuals, conversion, motion): ")
    ignore = input("What should be ignored (blog, footer, ecommerce, etc): ")

    return {
        "goal": goal,
        "style": style,
        "focus": focus,
        "ignore": ignore
    }

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <url>")
        sys.exit(1)

    url = sys.argv[1]

    context = ask_questions()

    print("\nAnalyzing website...\n")

    result = analyze_website(url, context)

    print("\n--- UX INTELLIGENCE REPORT ---\n")
    print(result)

if __name__ == "__main__":
    main()
