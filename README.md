# Grabsy

**Grabsy** is a simple and clean video download utility that supports various platforms. Just paste a video link and download it instantly in the best available quality.

---

## 🚀 Features

- 🔗 Paste link and download — super fast
- 🎥 Supports direct `.mp4` links and video platforms
- 🧩 Auto fallback between direct download and browser automation
- 💾 Downloads saved in `/downloads/` folder

---

## 🌐 Live Demo

**Website**: [https://grabsy-ai.onrender.com](https://grabsy-ai.onrender.com)

---

🧠 How It Works
User pastes the link and clicks "Download"

If it's a direct link (like .mp4), it downloads directly

Otherwise, it uses browser tools to fetch hidden video sources

Finally, the video is served for download

📁 Folder Structure
pgsql
Copy
Edit
grabsy_ai/
│
├── app.py
├── browser_sniffer.py
├── templates/
│   └── index.html
├── downloads/
└── requirements.txt

