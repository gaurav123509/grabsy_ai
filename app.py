from flask import Flask, request, send_file
import yt_dlp
import uuid
import os
import requests

app = Flask(__name__)

if not os.path.exists('downloads'):
    os.makedirs('downloads')

@app.route('/')
def home():
    return "🚀 Grabsy AI backend is running!"

@app.route('/download', methods=['POST'])
def download():
    url = request.form.get('url')
    if not url:
        return "❌ Error: No URL provided", 400

    video_id = str(uuid.uuid4())
    output_path = f"downloads/{video_id}.mp4"

    try:
        # First try yt-dlp
        try:
            ydl_opts = {
                'outtmpl': output_path,
                'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
                'noplaylist': True,
                'quiet': True,
                'nocheckcertificate': True,
                'skip_download': False,
                'retries': 3,
                'geo_bypass': True,
                'no_warnings': True,
                'ignoreerrors': False,
                'cookiefile': None,
                'username': None,
                'password': None,
                'usenetrc': False,
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            return send_file(output_path, as_attachment=True)

        except Exception as yt_error:
            # If yt-dlp fails, try direct download
            r = requests.get(url, stream=True, timeout=10)
            if r.status_code == 200:
                with open(output_path, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        f.write(chunk)
                return send_file(output_path, as_attachment=True)
            else:
                return f"❌ Error: Direct download failed. Status code: {r.status_code}", 400

    except Exception as e:
        return f"❌ Error: {str(e)}", 500
