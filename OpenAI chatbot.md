
# OpenAI GPT-3.5 Turbo Chatbot

## Description
This Python script uses OpenAI's `gpt-3.5-turbo` model to create a simple chatbot interface. Users can type in prompts, and the chatbot will generate responses based on OpenAI's language model. This is a continuous conversation until the user decides to exit by typing "quit," "exit," or "bye."

## Requirements
- Python 3.x
- OpenAI Python package (`openai`)
- An OpenAI API key

## Installation
1. Clone or download the repository.
2. Install the OpenAI library:
   ```bash
   pip install openai
   ```
3. Replace `[Your secret api key]` with your actual OpenAI API key in the code:
   ```python
   openai.api_key = "your_api_key_here"
   ```

## Usage
1. Run the script:
   ```bash
   python chatbot.py
   ```
2. Start chatting by typing messages. The chatbot will respond based on the prompt you provide.
3. Type `quit`, `exit`, or `bye` to end the conversation and exit the program.

## Example
```
You: Hello!
chatbot: Hello! How can I assist you today?
You: Tell me a joke.
chatbot: Why did the scarecrow win an award? Because he was outstanding in his field!
You: bye
```

## Important Notes
- **API Key**: Make sure you keep your API key safe and do not share it publicly.
- **OpenAI Account**: To use this script, you’ll need an OpenAI account with API access. Visit [OpenAI's website](https://platform.openai.com) to sign up and obtain your API key.

## License
This project is open-source and available under the MIT License.

---
