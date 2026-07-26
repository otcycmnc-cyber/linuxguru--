#!/bin/bash
sudo apt update && sudo apt install -y curl python3
curl -fsSL https://ollama.com/install.sh | sh
ollama pull llama3.2
chmod +x ai.py
sudo cp ai.py /usr/local/bin/ai
echo "Setup done. Try: ai \"hello\""