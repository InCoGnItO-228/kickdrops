```markdown
# KickAutoDrops Enhanced

[RU](README.ru.md) [EN](README.md)

> **Based on** [KickAutoDrops](https://github.com/PBA4EVSKY/kickautodrops) by [@PBA4EVSKY](https://github.com/PBA4EVSKY).  
> This enhanced version focuses on **Linux-first compatibility**, **automated setup**, and **improved user experience**.

---

**KickAutoDrops Enhanced** is a minimalist automation tool designed to efficiently collect **Rust game drops** from [Kick.com](https://kick.com) **without streaming any video or audio content**.  
The application runs in the background, simulating stream viewing by interacting directly with Kick.com's API—allowing you to collect drops while saving bandwidth and system resources.

---

## ⚙️ How It Works

Every **10 seconds**, the app simulates watching a stream by:
- Fetching stream metadata  
- Sending authenticated watch events to Kick.com  

This is **sufficient to progress drop timers**, while **completely bypassing video/audio downloads**.

To maintain accurate channel status (**ONLINE/OFFLINE**), the app establishes a **WebSocket connection** that receives real-time events about:
- Streams going online or offline  
- Game or category changes  
- Drop progress updates  
- Viewer count changes  

---

## 🧩 Installation

### Option 1: Pre-built Release (coming soon)

> *Linux/Windows/macOS binaries will be available in the [Releases](https://github.com/InCoGnItO-228/kickdrops-enhanced/releases) section after the first official release.*

### Option 2: Run from Source (recommended for Linux)

1. Install the **"Get cookies.txt LOCALLY"** browser extension:  
   - [Chrome](https://chromewebstore.google.com/detail/get-cookiestxt-locally/cclelndahbckbenkjhflpdbgdldlbecc)  
   - [Firefox](https://addons.mozilla.org/en-US/firefox/addon/get-cookies-txt-locally/)  
2. Go to [kick.com](https://kick.com) and log in  
3. Export all cookies and save them as **`cookies.txt`** in the project root  
4. Run once — everything sets up automatically:

```bash
git clone https://github.com/InCoGnItO-228/kickdrops-enhanced.git
cd kickdrops-enhanced
./run.sh
```

The `run.sh` script will:
- Create a virtual environment (`.venv`)  
- Install dependencies (`curl_cffi`, `websockets`)  
- Verify `cookies.txt` exists  
- Launch the app

> **Requirements**: Python 3.10+, Google Chrome (for cookie export), `libcurl` (usually preinstalled on Arch Linux)

---

### Option 3: Manual Build (optional)

```bash
git clone https://github.com/InCoGnItO-228/kickdrops-enhanced.git
cd kickdrops-enhanced

python -m venv .venv
source .venv/bin/activate

pip install curl_cffi websockets pyinstaller
pyinstaller index.spec  # executable will appear in dist/
```

---

## ❤️ Acknowledgements & Contributions

Original concept and implementation by **[@PBA4EVSKY](https://github.com/PBA4EVSKY)**.  
This project is an **enhanced, Linux-optimized fork** with automated setup and better stability.

Want to help?  
Feel free to **fork this repository** and submit a **pull request** — all contributions are welcome and appreciated! ❤️

---

## 📂 Project Structure

- `index.py` — main application logic  
- `run.sh` — automated Linux launcher  
- `cookies.txt` — your exported cookies (not committed)  
- `config.ini` — auto-generated settings  
- `.venv/` — isolated Python environment (not committed)
```
