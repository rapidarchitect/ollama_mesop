import mesop as me
import mesop.labs as mel

import ollama

# Set your model here
model = 'llama3'

@me.page(path="/chat")
def chat():
  mel.chat(transform)

def transform(prompt: str, history: list[mel.ChatMessage]) -> str:
  stream = ollama.chat(
    model = model,
    messages=[{'role': 'user', 'content': f'{history}\n{prompt}'}],
    stream=True,
  )

  for chunk in stream:
    yield(chunk['message']['content'])
