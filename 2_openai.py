import os
import openai
import sys

# Obtener la cadena de caracteres del primer argumento
question = sys.argv[1]

# Set your OpenAI API key from the environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": question}])

print(chat_completion.choices[0].message.content)