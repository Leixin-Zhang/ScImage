import requests
import json
import os
import pandas as pd
from tqdm import tqdm
import time
import shutil


# ALi Dashscope API key
API_KEY = "your_own_api_key"  # for API register link, please read README.md

#  API of Figure-generating LLM
REQ_URL = "https://dashscope.aliyuncs.com/api/v1/services/aigc/text2image/image-synthesis"

# Headers of the figure-generating requrest
REQ_HEADERS = {
    "X-DashScope-Async": "enable",
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# Headers of the figure-retrieving request
REC_HEADERS = {
    "Authorization": f"Bearer {API_KEY}"
}


def gen_pic(prompt: str, fig_path: str):
    """
    Asynchronous procedure:
    1. send figure-generating request which returns a task ID
    2. generate figure-downloading url according to the task ID
    3. send figure-retrieving request and save the figure
    Params:
    prompt: prompt of the figure
    fig_path: full path of the figure
    """
    # generate the content of figure-generating requrest
    request_contet = {
        "model": "wanx2.1-t2i-turbo",
        "input": {
            "prompt": f"{prompt}"
        },
        "parameters": {
            "size": "800*600",
            "n": 1
        }
    }
    # send a request to generate figure
    req_response = requests.post(REQ_URL, headers=REQ_HEADERS,
                                 data=json.dumps(request_contet))
    # get task ID for previous request
    task_id = req_response.json().get("output").get("task_id")
    # generate figure-retrieving url according to the task ID
    retrieve_url = f"https://dashscope.aliyuncs.com/api/v1/tasks/{task_id}"
    # wait for the figure to be generated
    time.sleep(10)
    # send a request to retrieve the figure asked to generate
    download_response = requests.get(retrieve_url, headers=REC_HEADERS)
    # get download url and save the figure
    download_url = download_response.json().get("output").get("results")[0].get("url")
    download_response = requests.get(download_url)
    with open(f'{fig_path}.png', 'wb') as file:
        file.write(download_response.content)


# Preparations
df = pd.read_excel(r"Attibution dict.xlsx")  # the Excel file in this repository
fig_path_prefix = os.getcwd() + r"/Scientific_graphs"
prompt_prefix = "Please generate a scientific figure according to the following requirements: "
if not os.path.exists(fig_path_prefix):
    os.mkdir(fig_path_prefix)

# Image generation in batches
for num in range(1, 5):
    initial_list = df[[f"Ex_ID{num}", f"Example_{num}"]].to_dict(orient="records")
    couple_list = dict()
    for one_set in initial_list:
        couple_list[one_set.get(f'Ex_ID{num}')] = one_set.get(f'Example_{num}')
    for key, val in tqdm(couple_list.items()):
        fig_path = fig_path_prefix + "/" + key + "_0"
        gen_pic(prompt_prefix + val, fig_path)

# Package images
shutil.make_archive(fig_path_prefix, 'zip', fig_path_prefix)
print("All file downloaded")
