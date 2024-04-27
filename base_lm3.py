
from openai import OpenAI

# ANSI escape codes for colors
YELLOW = '\033[93m'
RED = '\033[91m'
GREEN = '\033[92m'
RESET_COLOR = '\033[0m'


client = OpenAI(
    base_url='http://localhost:11434/v1/',
    api_key='ollama3',
)


def ask(user_input, system_message, conversation_history):
    conversation_history.append({"role": "user", "content": user_input})
    messages = [
        {"role": "system", "content": system_message},
        *conversation_history
    ]

    response = client.chat.completions.create(
        messages=messages,
        model='llama3',
        max_tokens=2000,
    )
    conversation_history.append({"role": "assistant", "content": response.choices[0].message.content})
    return response.choices[0].message.content

conversation_history = []
system_message = "You are an assistant that is an expert at extracting the most useful information from a given text."+\
    "You can help me with summarizing, extracting key points, and answering questions about the text. "+\
    "You can also help me with finding relevant information from the text. "+\
    "You can also help me with generating questions about the text. "+\
    "You can also help me with generating a quiz based on the text. "+\
    "You can also help me with generating a summary of the text. "+\
    "You can also help me with generating a title for the text. "+\
    "You can also help me with generating a conclusion for the text. "

print(RED + "Type 'quit' to exit" + RESET_COLOR)
while True:
    user_input = input(YELLOW + "User: " + RESET_COLOR)
    if user_input.lower() == 'quit':
        break
    response = ask(user_input, system_message, conversation_history)
    print(YELLOW + "Llama3: " + RESET_COLOR+ "\n" + GREEN + response + RESET_COLOR)
