# agents.py
from gtts import gTTS
import requests
from moviepy.editor import VideoFileClip, CompositeVideoClip
import os

PEXELS_API_KEY = os.getenv('Q1aOaDARtxRT3HKtuqeEXREGMSb3hMDmRXek3B8DhXaBLEmfA9ZufOL4')

class ContentInputAgent:
    def __init__(self):
        pass

    def get_script(self, script):
        return script

class AudioGeneratorAgent:
    def script_to_audio(self, script, filename='output.mp3'):
        tts = gTTS(text=script, lang='en')
        tts.save(filename)
        return filename

class VideoFetcherAgent:
    def fetch_stock_video(self, query, filename='video.mp4'):
        headers = {
            'Authorization': PEXELS_API_KEY
        }
        response = requests.get(f'https://api.pexels.com/videos/search?query={query}&per_page=1', headers=headers)
        video_url = response.json()['videos'][0]['video_files'][0]['link']
        video_data = requests.get(video_url).content
        with open(filename, 'wb') as f:
            f.write(video_data)
        return filename

class VideoEditorAgent:
    def combine_audio_video(self, audio_file, video_file, output_file='final_video.mp4'):
        video_clip = VideoFileClip(video_file)
        audio_clip = VideoFileClip(audio_file).audio
        final_clip = CompositeVideoClip([video_clip.set_audio(audio_clip)])
        final_clip.write_videofile(output_file)
        return output_file
