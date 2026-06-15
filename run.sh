#!/bin/bash

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

VENV_DIR=".venv"
PYTHON="$VENV_DIR/bin/python"
PIP="$VENV_DIR/bin/pip"

# === 1. System dependencies ===
echo "🔍 Checking system dependencies..."

# Check git
if ! command -v git &> /dev/null; then
    echo "❌ git not found. It is required to clone repositories."
    read -p "Install git? (Y/n): " -r
    if [[ ! $REPLY =~ ^[Nn]$ ]]; then
        sudo pacman -S --needed --noconfirm git
    else
        exit 1
    fi
fi

# Check Python
if ! command -v python &> /dev/null; then
    echo "❌ Python not found."
    read -p "Install Python? (Y/n): " -r
    if [[ ! $REPLY =~ ^[Nn]$ ]]; then
        sudo pacman -S --needed --noconfirm python python-pip
    else
        exit 1
    fi
fi

# Check build deps
BUILD_DEPS=("base-devel" "curl")
MISSING_DEPS=()
for dep in "${BUILD_DEPS[@]}"; do
    if ! pacman -Q "$dep" &> /dev/null; then
        MISSING_DEPS+=("$dep")
    fi
done

if [ ${#MISSING_DEPS[@]} -gt 0 ]; then
    echo "🔧 Missing system packages: ${MISSING_DEPS[*]}"
    echo "   Required to build 'curl_cffi'."
    read -p "Install them? (Y/n): " -r
    if [[ ! $REPLY =~ ^[Nn]$ ]]; then
        sudo pacman -S --needed --noconfirm "${MISSING_DEPS[@]}"
    else
        exit 1
    fi
fi

# === 2. cookies.txt validation ===
if [ ! -f "cookies.txt" ]; then
    echo "❌ cookies.txt not found!"
    echo "👉 Export cookies from https://kick.com using:"
    echo "   Chrome: https://chromewebstore.google.com/detail/get-cookiestxt-locally/cclelndahbckbenkjhflpdbgdldlbecc"
    exit 1
fi

if ! grep -q "kick.com" cookies.txt 2>/dev/null; then
    echo "⚠️ cookies.txt does not contain kick.com entries!"
    echo "Please export while logged in on https://kick.com"
    exit 1
fi
echo "✅ cookies.txt is valid."

# === 3. Virtual environment management ===
VENV_MARKER=".venv_path"

if [ -d "$VENV_DIR" ]; then
    if [ -f "$VENV_MARKER" ]; then
        SAVED_PATH=$(cat "$VENV_MARKER")
        CURRENT_PATH="$SCRIPT_DIR"
        if [ "$SAVED_PATH" != "$CURRENT_PATH" ]; then
            echo "⚠️ Project moved from $SAVED_PATH to $CURRENT_PATH"
            echo "   Recreating virtual environment..."
            rm -rf "$VENV_DIR"
            rm -f "$VENV_MARKER"
        fi
    else
        # First run after manual .venv creation — mark it
        echo "$SCRIPT_DIR" > "$VENV_MARKER"
    fi
fi

if [ ! -d "$VENV_DIR" ]; then
    echo "🔧 Creating virtual environment..."
    python -m venv "$VENV_DIR"
    echo "$SCRIPT_DIR" > "$VENV_MARKER"
    "$PYTHON" -m pip install --upgrade pip
fi

# === 4. Install dependencies ===
echo "📦 Installing Python dependencies..."
"$PIP" install -q curl_cffi websockets

# === 5. Run ===
echo "🚀 Starting KickAutoDrops Enhanced..."
"$PYTHON" index.py
