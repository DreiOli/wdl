#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import youtube_dl

import ffmpeg

import ffprobe


# In[ ]:


def run():
    video_url = input("please enter youtube video url:")
    video_info = youtube_dl.YoutubeDL().extract_info(
        url = video_url,download=False
    )
    filename = f"{video_info['title']}.mp3"
    options = {
    'format':'bestaudio/best',
    'extractaudio':True,
    'audioformat':'mp3',
    'outtmpl':'%(id)s.%(ext)s',     #name the file the ID of the video
    'noplaylist':True,
    'nocheckcertificate':True,
    'proxy':"",
    'addmetadata':True,
    'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        },
        {
            'key': 'FFmpegMetadata'
        }],
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    print("Download complete... {}".format(filename))

if __name__=='__main__':
    run()
