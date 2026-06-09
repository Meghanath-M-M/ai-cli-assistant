# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "groq",
#     "pydantic",
#     "python-dotenv",
# ]
# ///

import os
import sys
import argparse
import logging
from ai_cli.agent import AIAgent


def main():
    parser = argparse.ArgumentParser(
        description="AI Code Assistant - A conversational AI agent with file editing capabilities"
    )
    parser.add_argument("--api-key", help="GROQ API key (or set GROQ_API_KEY env var)")
    args = parser.parse_args()

    api_key = args.api_key or os.environ.get("GROQ_API_KEY")
    if not api_key:
        print(
            "Error: Please provide an API key via --api-key or GROQ_API_KEY environment variable"
        )
        sys.exit(1)

    agent = AIAgent(api_key)

    print("AI Code Assistant")
    print("================")
    print("A conversational AI agent that can read, list, and edit files.")
    print("Type 'exit' or 'quit' to end the conversation.")
    print()

    while True:
        try:
            user_input = input("You: ").strip()

            if user_input.lower() in ["exit", "quit"]:
                print("Goodbye!")
                break

            if not user_input:
                continue

            print("\nAssistant: ", end="", flush=True)
            response = agent.chat(user_input)
            print(response)
            print()

        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"\nError: {str(e)}")
            print()


if __name__ == "__main__":
    main()
