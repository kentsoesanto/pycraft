# PyCraft Editor

A modern Python IDE with local AI assistance powered by Ollama.

## Features

- 🐍 **Python Code Editor** with syntax highlighting
- 🤖 **Local AI Assistant** (AstroBot) powered by Ollama
- ⚡ **Real-time Code Execution** 
- 📁 **File Management** with SQLite database
- 🎨 **Modern UI** with dark/light themes
- 🔧 **Code Analysis** and suggestions

## Prerequisites

### Required Software
1. **Node.js** (v18 or higher)
   - Download from [nodejs.org](https://nodejs.org/)
   - Verify installation: `node --version`

2. **Python** (3.8 or higher)
   - Download from [python.org](https://python.org/)
   - Verify installation: `python --version`

3. **Ollama** (for AI features)
   - Download from [ollama.ai](https://ollama.ai/)
   - Install and run: `ollama serve`

## Quick Start

### 1. Extract the ZIP file
```bash
# Extract to your desired location
unzip PyCraft-Editor.zip
cd PyCraft-Editor
```

### 2. Install Dependencies
```bash
npm install
```

### 3. Start the Application
```bash
npm run dev
```

### 4. Open in Browser
Navigate to: `http://127.0.0.1:5000`

## Usage

### Basic Python Coding
1. Open the editor
2. Write Python code
3. Click "Run Terminal" to execute

### AI Assistant (AstroBot)
1. **Start Ollama**: `ollama serve`
2. **Load a model**: `ollama pull deepseek-r1:14b`
3. Use the chat interface to get AI assistance

### Offline Mode
- Works without Ollama for basic Python coding
- Shows "AstroBot is Offline, Please Switch Her ON" when AI is unavailable

## Project Structure

```
PyCraft-Editor/
├── client/                 # React frontend
│   ├── src/
│   │   ├── components/     # UI components
│   │   ├── pages/         # Main pages
│   │   └── lib/           # Utilities
├── server/                # Express backend
│   ├── routes.ts          # API endpoints
│   ├── db.ts             # Database setup
│   └── pythonManager.ts   # Python execution
├── shared/                # Shared schemas
├── package.json           # Dependencies
└── README.md             # This file
```

## Troubleshooting

### Port Already in Use
```bash
# Kill existing processes
taskkill /f /im node.exe
# Then restart
npm run dev
```

### Python Not Found
- Ensure Python is installed and in PATH
- Try: `python --version`

### Ollama Connection Issues
- Verify Ollama is running: `ollama serve`
- Check if model is installed: `ollama list`
- Install model: `ollama pull deepseek-r1:14b`

### Database Errors
```bash
# Reset database (if needed)
npm run db:push
```

## Development

### Available Scripts
- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run db:push` - Update database schema

### Environment Variables
- `NODE_ENV` - Set to `development` or `production`
- `DATABASE_URL` - SQLite database path (auto-configured)

## Support

For issues or questions:
1. Check the troubleshooting section
2. Verify all prerequisites are installed
3. Check the console for error messages

## License

This project is open source and available under the MIT License. 