import gradio as gr
import numpy as np
import time


def fake_diffusion(steps):
    for _ in range(steps):
        time.sleep(1)
        image = np.random.random((600, 600, 3))
        yield image
    
    image = "https://i.picsum.photos/id/867/600/600.jpg?hmac=qE7QFJwLmlE_WKI7zMH6SgH5iY5fx8ec6ZJQBwKRT44" 
    yield image


demo = gr.Interface(fake_diffusion, 
                    inputs=gr.Slider(1, 10, 3), 
                    outputs="image")
demo.queue()

if __name__ == "__main__":
    demo.launch()
