import streamlit as st
import openai

OPENAI_API_KEY = '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'



client = openai.OpenAI(api_key='sk-xKt0iG5AGjLp66sGj3xlT3BlbkFJy4MKEGnXAp3gCcj7JdG1f')

try:
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
    {
      "role": "user",
      "content": "hello world - what is the answer to the universe and all the rest?"
    }
    ],
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    print(response)
except client.APIError as e:
    print(f"Failed to connect to OpenAI API: {e}")
    pass
