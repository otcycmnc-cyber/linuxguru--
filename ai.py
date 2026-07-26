#!/usr/bin/env python3
import sys, subprocess

SYSTEM_PROMPT = """You are a terminal-based coding, networking, and cybersecurity tutor.
Rules:
- If the user pastes code, find bugs and reply with the corrected code plus a short explanation.
- If the user asks about networking or cybersecurity concepts, explain clearly with simple real-world examples.
- Keep answers short and practical, suited for reading in a terminal.
"""

def ask(prompt, model="llama3.2"):
    full_prompt = SYSTEM_PROMPT + "\n\nUser input:\n" + prompt
    result = subprocess.run(
        ["ollama", "run", model],
        input=full_prompt,
        capture_output=True, text=True
    )
    print(result.stdout.strip())

if __name__ == "__main__":
    if not sys.stdin.isatty():
        piped = sys.stdin.read()
        question = " ".join(sys.argv[1:])
        prompt = (question + "\n" + piped) if question else piped
    else:
        if len(sys.argv) < 2:
            print('Usage: ai "your question"   OR   cat file.py | ai "fix this"')
            sys.exit(1)
        prompt = " ".join(sys.argv[1:])
    ask(prompt)