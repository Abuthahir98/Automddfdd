# coordinator.py
from agents import ContentInputAgent, AudioGeneratorAgent, VideoFetcherAgent, VideoEditorAgent

class CoordinatorAgent:
    def __init__(self):
        self.content_input = ContentInputAgent()
        self.audio_generator = AudioGeneratorAgent()
        self.video_fetcher = VideoFetcherAgent()
        self.video_editor = VideoEditorAgent()

    def create_video(self, script, keywords):
        audio_file = self.audio_generator.script_to_audio(script)
        video_file = self.video_fetcher.fetch_stock_video(keywords)
        final_video = self.video_editor.combine_audio_video(audio_file, video_file)
        return final_video
