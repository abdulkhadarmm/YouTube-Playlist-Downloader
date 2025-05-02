# 📺 YouTube Playlist Downloader (GUI)

A simple Python GUI application to download **entire YouTube playlists** in your selected quality (e.g., 360p, 720p, 1080p) using `yt-dlp` and `ffmpeg`.

---

## 🚀 Features

- Clean GUI to input playlist URL.
- Fetch and display video/audio formats from the **first video**.
- Choose quality like 360p, 720p, 1080p for **all videos** in the playlist.
- Automatically downloads video and audio, then merges them using ffmpeg.
- Logs live download progress in a scrollable output panel.

---

## 🧰 Requirements

### 📦 For Windows (Recommended via [Scoop](https://scoop.sh))

Install Scoop (if not already installed):

```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
irm get.scoop.sh | iex
```

Then install the required tools:

```powershell
scoop install python
scoop install yt-dlp
scoop install ffmpeg
```

✅ Ensure Scoop's `shims` directory is in your system PATH so tools are globally accessible.

### 💻 For macOS/Linux

#### macOS (via Homebrew):

```bash
brew install python
brew install ffmpeg
brew install yt-dlp
```

#### Ubuntu/Debian:

```bash
sudo apt update
sudo apt install python3 python3-pip ffmpeg -y
pip3 install yt-dlp
```

---

## 📂 How to Run

1. Clone this repo or download the `Youtube-Playlist-Downloader.py` script.
2. Open terminal or PowerShell and navigate to the project directory.
3. Run the application:

```bash
git clone https://github.com/abdulkhadarmm/YouTube-Playlist-Downloader.git
cd YouTube-Playlist-Downloader
python Youtube-Playlist-Downloader.py
```

If you're on Linux/macOS, you might need to use:

```bash
python3 Youtube-Playlist-Downloader.py
```

---

## 🔐 Permissions Note

If you're running Scoop for the first time:

```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

If you see command-not-found errors, ensure Scoop's `shims` path is added to your `PATH` environment variable.

---

## 🖼️ Screenshot

*Coming soon*

---


## 🧑‍💻 How to Use

1. Launch the app using the instructions above.
2. Paste the playlist URL into the URL input field.
3. Click **Fetch Formats** to load available video/audio formats.
4. Select the desired video and audio quality (e.g., 137 - 1080p, 140 - m4a) from the dropdowns.
5. Click **Download & Merge** to begin downloading.
6. Wait for the process to complete. A message box will notify you upon successful download.


## 📝 License

This project is open-source and available under the [MIT License](LICENSE).
