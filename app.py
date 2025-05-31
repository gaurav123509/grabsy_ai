@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
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
        'cookiefile': None,  # Force no cookies
        'username': None,
        'password': None,
        'usenetrc': False,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return send_file(output_path, as_attachment=True)
    except Exception as e:
        return f"❌ Error: {str(e)}"