#!/bin/bash

echo "========================================"
echo "   PyCraft Editor - Starting Up"
echo "========================================"
echo

echo "Checking Node.js installation..."
if ! command -v node &> /dev/null; then
    echo "ERROR: Node.js is not installed or not in PATH"
    echo "Please install Node.js from https://nodejs.org/"
    exit 1
fi

echo "Checking Python installation..."
if ! command -v python &> /dev/null && ! command -v python3 &> /dev/null; then
    echo "WARNING: Python is not installed or not in PATH"
    echo "Some features may not work properly"
    echo "Please install Python from https://python.org/"
    echo
fi

echo "Installing dependencies..."
npm install

echo
echo "Starting PyCraft Editor..."
echo
echo "The application will open at: http://127.0.0.1:5000"
echo
echo "To enable AI features:"
echo "1. Install Ollama from https://ollama.ai/"
echo "2. Run: ollama serve"
echo "3. Run: ollama pull deepseek-r1:14b"
echo
echo "Press Ctrl+C to stop the server"
echo

npm run dev 