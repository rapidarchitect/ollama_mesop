import mesop as me
import mesop.labs as mel

import ollama

# Set your model here
model = 'llama3'

@me.page(path="/chat")
def chat():
  """
  This function is responsible for handling the "/chat" route and interacting with the OpenAI GPT model to generate responses based on user input.
  :return: str
  """
  mel.chat(transform)

def transform(prompt: str, history: list[mel.ChatMessage]) -> str:
  """
  This function takes a prompt and a history of previous user inputs and generates a response using the OpenAI GPT model from the Ollama library.
  
  Args:
    prompt (str): The user's input or question.
    history (list[mel.ChatMessage]): A list of previous user inputs and corresponding responses.

  Returns:
    str: The generated response using GPT model.
  """
  stream = ollama.chat(
    model = model,
    messages=[{'role': 'user', 'content': f'{history}\n{prompt}'}],
    stream=True,
  )

  for chunk in stream:
    yield(chunk['message']['content'])
