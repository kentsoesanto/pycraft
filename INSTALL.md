# PyCraft Editor - Quick Installation Guide

## 🚀 5-Minute Setup

### Step 1: Install Required Software

**Windows Users:**
1. **Node.js**: Download from [nodejs.org](https://nodejs.org/) (LTS version)
2. **Python**: Download from [python.org](https://python.org/) (3.8+)
3. **Ollama**: Download from [ollama.ai](https://ollama.ai/)

**macOS Users:**
```bash
# Using Homebrew
brew install node python ollama
```

**Linux Users:**
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install nodejs npm python3
curl -fsSL https://ollama.ai/install.sh | sh
```

### Step 2: Extract and Install

1. **Extract** the ZIP file to any folder
2. **Open Command Prompt/Terminal** in the extracted folder
3. **Run**: `npm install`
4. **Start**: `npm run dev`
5. **Open**: http://127.0.0.1:5000

### Step 3: Enable AI Features (Optional)

```bash
# Start Ollama
ollama serve

# In another terminal, install a model
ollama pull deepseek-r1:14b
```

## ✅ Verification

**Check if everything works:**
- ✅ **Node.js**: `node --version` (should show v18+)
- ✅ **Python**: `python --version` (should show 3.8+)
- ✅ **App**: http://127.0.0.1:5000 loads
- ✅ **AI**: Chat with AstroBot (if Ollama is running)

## 🆘 Common Issues

**"Port already in use"**
```bash
taskkill /f /im node.exe
npm run dev
```

**"Python not found"**
- Install Python from python.org
- Make sure to check "Add to PATH" during installation

**"AstroBot is Offline"**
- Start Ollama: `ollama serve`
- Install model: `ollama pull deepseek-r1:14b`

## 📞 Need Help?

1. Check the main README.md for detailed instructions
2. Verify all software is properly installed
3. Check console for error messages

**Your PyCraft Editor is ready to use!** 🎉 