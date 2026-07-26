#!/usr/bin/env python3
import sys, subprocess

def ask(question, model="llama3.2"):
    result = subprocess.run(
        ["ollama", "run", model, question],
        capture_output=True, text=True
    )
    print(result.stdout.strip())

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: ai "your question"')
        sys.exit(1)
    ask(" ".join(sys.argv[1:]))