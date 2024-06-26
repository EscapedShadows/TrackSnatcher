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

def get_title(url, oauth=False):
    from pytube import YouTube

    yt = YouTube(
        url,
        use_oauth=oauth,
        allow_oauth_cache=oauth
    )

    return yt.title