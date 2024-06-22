import mesop as me
import mesop.labs as mel

import ollama

@me.page(path="/chat")
def chat():
  mel.chat(transform)

def transform(prompt: str, history: list[mel.ChatMessage]) -> str:
  response = ollama.chat(model='llama3',messages=[
  {
    'role': 'user',
    'content': f'{history} \n {prompt}',
  },
])
  return response['message']['content']
