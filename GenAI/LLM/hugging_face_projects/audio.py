import numpy as np
import gradio as gr


def reverse_audio(audio):
    sr, data = audio
    reversed_audio = (sr, np.flipud(data))
    return reversed_audio


mic = gr.Audio(source="microphone", type="numpy", label="Speak here...")
# gr.Interface(reverse_audio, mic, "audio").launch()