from openai import OpenAI 
import pandas as pd
import requests 
import os




client = OpenAI(api_key=os.getenv("OPENAI_API_KEY", '...'))


def gpt_4o_gen(prompt):

    stream = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": prompt}],
    stream=True,
    )

    path = ...
    with open(path, "w",encoding="utf-8") as file:
        for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                file.write(chunk.choices[0].delta.content)


def gpt_o1_gen(prompt):
    completion = client.chat.completions.create(
        model="o1-preview",
        messages=[
            {"role": "user","content": prompt}]
    )

    path = ...
    with open(path, "w",encoding="utf-8") as file:
        file.write(completion.choices[0].message.content)



def dalle_gen(generation_prompt):
    response = client.images.generate(
        model="dall-e-3",
        prompt=generation_prompt,
        n=1,
        size="1024x1024",
        response_format="url"
    )
    image_url = response.data[0].url 
    image_response = requests.get(image_url)
    image_path = ...
    with open(image_path, "wb") as file:
        file.write(image_response.content)

