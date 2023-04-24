import os
import openai
import requests
import csv
from helper_functions import synthesize_speech
import uuid
import asyncio

def make_request(system_prompt, user_prompt):
    TOKEN = os.environ.get('OPENAI_API_KEY')

    print(TOKEN)
    header = {
            'authorization': f'Bearer {TOKEN}',
            'content-type': 'application/json'
        }

    URL = "https://api.openai.com/v1/chat/completions"

    messages = [
        {"role": "system", "content": f'{system_prompt}'},
        {"role": "user", "content": f'{user_prompt}'}
    ]

    data = {
        "model": "gpt-3.5-turbo",
        "messages": messages,
        "temperature": 0.2
    }

    response = requests.post(
        URL,
        json=data,
        headers=header
    )

    response = response.json()

    return response

with open('prompts/system-prompt.txt', "r") as f:
    system_prompt = f.read()

with open('prompts/user-prompt.txt', "r") as f:
    user_prompt = f.read()

book_title = 'test'

unique_id = str(uuid.uuid4())

# answer_file_path = f'../{book_title}-{unique_id}.ssml'

answer_file_path = f'../{book_title}-.ssml'


# response = make_request(system_prompt, user_prompt)

# print(response)

# choices = response['choices']
# message = choices[0]['message']
# content = message['content']

# with open(answer_file_path, "w") as f:
#     f.write(content)

synthesize_speech(answer_file_path, unique_id)

#asyncio.run(coro_obj)
