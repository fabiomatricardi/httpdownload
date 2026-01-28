
# httpdownload 🖥️


**One command. Zero hassle. Beautiful downloads.**

```bash
httpdownload "https://github.com/user/repo/blob/main/file.gif"
```

Downloads files with a **Rich progress bar** and **auto-fixes GitHub blob→raw URLs**.

<img width="1664" height="928" alt="1769522496" src="https://github.com/user-attachments/assets/30af4f95-4c57-41a5-94a6-006784d28db0" />

## ✨ Features

- ✅ **Single command**: `httpdownload <URL>`
- 📊 **Live progress**: Size, speed, ETA with Rich
- 🔮 **GitHub magic**: `blob` → `raw` automatically
- 💾 **Smart naming**: Uses filename from URL
- 🚀 **Streaming**: Handles huge files efficiently
- 📦 **Pip installable**: Real CLI tool


## 🎬 Live Demo

```
Downloading GLINER-TEXTUAL.gif [██████████████░░░░░░░░] 67% 2.3MB/3.5MB 450KB/s 00:12
```


## 🚀 Quick Start

```bash
# Install
pip install .

# Or editable install (recommended for dev)
pip install -e .

# Download anything
httpdownload "https://github.com/fabiomatricardi/GliNER2-textual-app/blob/main/GLINER-TEXTUAL.gif"

# Regular URLs work too
httpdownload "https://example.com/file.zip"
```


## 📁 Project Structure

```
httpdownload/
├── httpdownload/
│   ├── __init__.py     # Package marker + version
│   └── cli.py          # Core logic
└── pyproject.toml      # Modern packaging
```


## 🛠️ How It Works

1. **Normalizes URL** (GitHub blob→raw)
2. **Streams download** (chunk by chunk)
3. **Rich progress bar** (speed, ETA, size)
4. **Saves to current dir** with URL filename

## 🎯 Why Not `wget`?

| `wget` | `httpdownload` |
| :-- | :-- |
| `wget -O- --no-check-certificate ...` | `httpdownload <URL>` |
| No progress by default | Beautiful live progress |
| GitHub blob URLs fail | Auto-converts to raw |
| 20+ flags to remember | Zero config |

## 🔧 Development

```bash
git clone <repo>
cd httpdownload
pip install -e .
# Now `httpdownload` is available globally
```

**Dependencies**: `requests`, `rich`

## 📖 Article

Read how this tool was built with AI assistance: [From Annoyance to CLI Magic](LINK-TO-MEDIUM)

## 🙌 Thanks

Built with help from AI pair programming. Perfect example of turning frustration into tools.

---

[![Star History](https://img.shields.io/github/stars/fabiomatricardi/httpdownload.svg?style=social&label=%E2%AD%90)](https://github.com/fabiomatricardi/httpdownload/stargazers/)
