import gradio as gr

gr.Interface(fn=predict, inputs="text", outputs="text").launch()