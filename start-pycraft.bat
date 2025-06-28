@echo off
echo ========================================
echo    PyCraft Editor - Starting Up
echo ========================================
echo.

echo Checking Node.js installation...
node --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Node.js is not installed or not in PATH
    echo Please install Node.js from https://nodejs.org/
    pause
    exit /b 1
)

echo Checking Python installation...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo WARNING: Python is not installed or not in PATH
    echo Some features may not work properly
    echo Please install Python from https://python.org/
    echo.
)

echo Installing dependencies...
npm install

echo.
echo Starting PyCraft Editor...
echo.
echo The application will open at: http://127.0.0.1:5000
echo.
echo To enable AI features:
echo 1. Install Ollama from https://ollama.ai/
echo 2. Run: ollama serve
echo 3. Run: ollama pull deepseek-r1:14b
echo.
echo Press Ctrl+C to stop the server
echo.

npm run dev

pause 