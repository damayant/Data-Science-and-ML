import gradio as gr


def greet(name):
    return "Hello " + name


demo = gr.Interface(fn=predict, inputs="text", outputs="text")

demo.launch()