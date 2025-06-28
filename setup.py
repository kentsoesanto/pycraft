#!/usr/bin/env python3
"""
PyCraft Editor Setup Verification Script
This script checks if all required software is installed correctly.
"""

import sys
import subprocess
import os
import platform

def check_command(command, description):
    """Check if a command is available."""
    try:
        result = subprocess.run([command, '--version'], 
                              capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            version = result.stdout.strip().split('\n')[0]
            print(f"✅ {description}: {version}")
            return True
        else:
            print(f"❌ {description}: Not found")
            return False
    except (subprocess.TimeoutExpired, FileNotFoundError):
        print(f"❌ {description}: Not found")
        return False

def main():
    print("=" * 50)
    print("    PyCraft Editor - Setup Verification")
    print("=" * 50)
    print()
    
    system = platform.system()
    print(f"Operating System: {system}")
    print()
    
    # Check Node.js
    node_ok = check_command('node', 'Node.js')
    
    # Check npm
    npm_ok = check_command('npm', 'npm')
    
    # Check Python
    python_ok = check_command('python', 'Python')
    if not python_ok:
        python_ok = check_command('python3', 'Python3')
    
    # Check Ollama (optional)
    ollama_ok = check_command('ollama', 'Ollama')
    
    print()
    print("=" * 50)
    print("Setup Summary:")
    print("=" * 50)
    
    if node_ok and npm_ok and python_ok:
        print("✅ All required software is installed!")
        print("🚀 You can now run: npm install && npm run dev")
    else:
        print("❌ Some required software is missing:")
        if not node_ok:
            print("   - Install Node.js from https://nodejs.org/")
        if not npm_ok:
            print("   - npm should come with Node.js")
        if not python_ok:
            print("   - Install Python from https://python.org/")
    
    if ollama_ok:
        print("🤖 Ollama is installed - AI features will be available!")
    else:
        print("⚠️  Ollama not found - Install from https://ollama.ai/ for AI features")
    
    print()
    print("For detailed instructions, see README.md")
    print("For quick setup, see INSTALL.md")

if __name__ == "__main__":
    main() 