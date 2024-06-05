# app.py
from coordinator import CoordinatorAgent
import gradio as gr

coordinator = CoordinatorAgent()

def create_video(script, keywords):
    return coordinator.create_video(script, keywords)

iface = gr.Interface(
    fn=create_video,
    inputs=[gr.Textbox(label="Enter Content Script"), gr.Textbox(label="Enter Keywords for Video")],
    outputs=gr.File(label="Generated Video"),
    title="Automated Video Creator",
    description="Enter a content script and keywords to generate a video with audio and stock footage."
)

if __name__ == "__main__":
    iface.launch()
