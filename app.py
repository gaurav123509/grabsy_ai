# app.py mein yeh code add karo direct .mp4 ke liye

import requests

@app.route('/download', methods=['POST'])
def download():
    url = request.form.get('url')
    if not url:
        return "❌ Error: No URL provided", 400

    video_id = str(uuid.uuid4())
    output_path = f"downloads/{video_id}.mp4"

    try:
        if url.endswith(".mp4"):
            # Handle direct MP4 URLs
            r = requests.get(url, stream=True)
            if r.status_code == 200:
                with open(output_path, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        f.write(chunk)
                return send_file(output_path, as_attachment=True)
            else:
                return f"❌ Error: Failed to download. Status code: {r.status_code}", 400
        else:
            # Use yt-dlp for streaming platforms
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

    except Exception as e:
        return f"❌ Error: {str(e)}", 500
