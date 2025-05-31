from flask import Flask, request, send_file, render_template
import yt_dlp
import uuid
import os

app = Flask(__name__)

# Ensure downloads folder exists
if not os.path.exists('downloads'):
    os.makedirs('downloads')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form.get('url')
    if not url:
        return "❌ Error: No URL provided", 400

    video_id = str(uuid.uuid4())
    output_path = f"downloads/{video_id}.mp4"

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

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return send_file(output_path, as_attachment=True)
    except Exception as e:
        return f"❌ Error: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)
