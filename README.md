
# 🛡️ Security Monitor

A lightweight Python + Flask project for logging visitor IP and User-Agent info in a local JSON file. Great for learning about request headers, logging, and basic security awareness.

## 🚀 Features
- Logs IP address and user agent
- Parses browser, OS, and device info
- Stores logs in JSON format
- Uses `user-agents` library for deep analysis

## 📦 Installation

```bash
pip install -r requirements.txt
```

## 🔧 Usage

```bash
python app.py
```

Then visit: `http://127.0.0.1:5000` in your browser.

## 🧠 Output Sample

```json
{
  "ip": "127.0.0.1",
  "user_agent": "Mozilla/5.0...",
  "browser": "Firefox 113.0",
  "os": "Windows 10",
  "device": "Other",
  "time": "2025-05-13T09:00:00"
}
```

## 💡 Future Ideas
- GeoIP lookup
- Alerts on unknown devices
- Web dashboard for live logs
