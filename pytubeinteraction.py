def get_tracks(urls, oauth=False):
    from pytube import YouTube

    streams = []

    for url in urls:
        yt = YouTube(
            url,
            use_oauth=oauth,
            allow_oauth_cache=oauth
        )

        stream = yt.streams.filter(only_audio=True).first()

        streams.append(stream)

    return streams

def get_titles(urls, oauth=False):
    from pytube import YouTube

    titles = []

    for url in urls:
        yt = YouTube(
            url,
            use_oauth=oauth,
            allow_oauth_cache=oauth
        )

        title = yt.title.replace('\u200b', '').replace('\u2060', '')

        titles.append(title)
    
    return titles

def get_id(url, oauth=False):
    from pytube import YouTube

    yt = YouTube(
        url,
        use_oauth=oauth,
        allow_oauth_cache=oauth
    )

    vId = yt.video_id

    return vId