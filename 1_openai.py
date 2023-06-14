import os
import openai

# Set your OpenAI API key from the environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

# list models
models = openai.Model.list()

# print the first model's id
for i in range(len(models.data)):
    print(models.data[i].id)