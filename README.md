# Mesop Chatbot Integration with Ollama

## Why use this?
This project uses the new Google Mesop library to quickly create user interfaces. Bot files are less than 50 lines of code including docs.

This repository contains a Python script that integrates the Mesop chatbot framework (`mesop` and `mesop.labs`) with the Ollama library to create an interactive chat application using OpenAI GPT models. The application can be accessed via a specific route ("/chat") in your web application.

## Prerequisites
To run this script, you need to have the following libraries installed:

* Mesop and Mesop Labs
* Ollama

You can install them using `pip`:
```bash
pip install mesop mesop.labs ollama
```

## Usage

To launch your chat run the following from your terminal

```bash
mesop ol_mesop.py
```

### OR for the streaming version ###

```bash
mesop ol_stream_mesop.py
```

Then open your browser to http://localhost:32123/chat

#License

This project is licensed under the MIT License - see the LICENSE file for details.
