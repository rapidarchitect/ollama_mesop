import mesop as me
import mesop.labs as mel
import ollama

# default model to starling-lm for fast testing, change to a model you have installed in ollama
model = 'starling-lm'

@me.page(path="/chat")
def chat():
  """
  This function is responsible for handling the "/chat" route and interacting with the OpenAI GPT model to generate responses based on user input.
  :return: str
  """
  try:
    response = mel.chat(transform)
  except Exception as e:
    print("An error occurred while trying to chat:", e)

def transform(prompt: str, history: list[mel.ChatMessage]) -> str:
  """
  This function takes a prompt and a history of previous user inputs and generates a response using the OpenAI GPT model from the Ollama library.
  
  Args:
    prompt (str): The user's input or question.
    history (list[mel.ChatMessage]): A list of previous user inputs and corresponding responses.

  Returns:
    str: The generated response using GPT model.
  """
  try:
    response = ollama.chat(model=model, messages=[
      {
        'role': 'user',
        'content': f'{history} \n {prompt}',
      },
    ])
  except Exception as e:
    print("An error occurred while generating the response:", e)
    return ""
  
  return response['message']['content']
