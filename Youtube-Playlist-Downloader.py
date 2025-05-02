import subprocess
import os
import tkinter as tk
from tkinter import messagebox, filedialog

# Globals to hold format selections
video_formats = []
audio_formats = []

# Fetch available formats from the first video in the playlist
def fetch_formats():
    global video_formats, audio_formats
    url = url_entry.get().strip()
    if not url:
        messagebox.showerror("Error", "Enter a YouTube Playlist URL.")
        return

    output_text.delete("1.0", tk.END)
    video_formats.clear()
    audio_formats.clear()
    video_menu['menu'].delete(0, 'end')
    audio_menu['menu'].delete(0, 'end')

    try:
        # Get the URL of the first video in the playlist
        result = subprocess.run(["yt-dlp", "--flat-playlist", "--print", "%(url)s", url],
                                capture_output=True, text=True)
        first_video_url = result.stdout.strip().splitlines()[0]

        # Fetch format info from the first video
        result = subprocess.run(["yt-dlp", "-F", first_video_url], capture_output=True, text=True)
        output_text.insert(tk.END, result.stdout)

        for line in result.stdout.splitlines():
            if not line.strip() or not line.strip()[0].isdigit():
                continue
            parts = line.split()
            if len(parts) < 5:
                continue

            format_id = parts[0]
            ext = parts[1]
            resolution = parts[2] if 'x' in parts[2] or 'p' in parts[2] else ''

            if "video" in line and "audio" not in line:
                res_label = resolution.split('x')[1] + "p" if 'x' in resolution else resolution
                label = f"{format_id} - {res_label}"
                video_formats.append((format_id, label))
            elif "audio" in line:
                label = f"{format_id} - {ext}"
                audio_formats.append((format_id, label))

        if not video_formats or not audio_formats:
            messagebox.showerror("Error", "No suitable formats found.")
            return

        for code, label in video_formats:
            video_menu['menu'].add_command(label=label, command=tk._setit(selected_video, code))

        for code, label in audio_formats:
            audio_menu['menu'].add_command(label=label, command=tk._setit(selected_audio, code))

        selected_video.set(video_formats[0][0])
        selected_audio.set(audio_formats[0][0])

    except Exception as e:
        messagebox.showerror("Error", str(e))


# Download and merge all videos in the playlist using selected format
def download_playlist():
    url = url_entry.get().strip()
    v_code = selected_video.get()
    a_code = selected_audio.get()
    if not url or not v_code or not a_code:
        return

    download_dir = filedialog.askdirectory(title="Select Download Folder")
    if not download_dir:
        return

    output_template = os.path.join(download_dir, "%(playlist_index)s - %(title)s.%(ext)s")

    cmd = [
        "yt-dlp",
        "-f", f"{v_code}+{a_code}",
        "--yes-playlist",
        "-o", output_template,
        url
    ]

    output_text.insert(tk.END, f"\nDownloading playlist using formats: Video({v_code}), Audio({a_code})...\n")
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1)
    for line in process.stdout:
        output_text.insert(tk.END, line)
        output_text.see(tk.END)
        output_text.update()
    process.wait()

    if process.returncode != 0:
        messagebox.showerror("Error", "Download failed.")
        return

    messagebox.showinfo("Done", "✅ Playlist downloaded successfully!")

# GUI Setup
root = tk.Tk()
root.title("YouTube Playlist Downloader")
root.geometry("800x600")

# URL input
tk.Label(root, text="YouTube Playlist URL:").pack(pady=5)
url_entry = tk.Entry(root, width=90)
url_entry.pack()

# Format selectors
format_frame = tk.Frame(root)
format_frame.pack(pady=10)

tk.Label(format_frame, text="Video Format:").grid(row=0, column=0, padx=5)
selected_video = tk.StringVar()
video_menu = tk.OptionMenu(format_frame, selected_video, "")
video_menu.config(width=40)
video_menu.grid(row=0, column=1, padx=5)

tk.Label(format_frame, text="Audio Format:").grid(row=0, column=2, padx=5)
selected_audio = tk.StringVar()
audio_menu = tk.OptionMenu(format_frame, selected_audio, "")
audio_menu.config(width=40)
audio_menu.grid(row=0, column=3, padx=5)

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Fetch Formats", command=fetch_formats).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Download Playlist", command=download_playlist).pack(side=tk.LEFT, padx=5)

# Output log
output_text = tk.Text(root, wrap="none", height=20)
output_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

root.mainloop()
