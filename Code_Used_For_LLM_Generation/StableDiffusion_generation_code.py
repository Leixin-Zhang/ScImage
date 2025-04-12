import requests
import pandas as pd
import os
from os.path import join
from tqdm import tqdm
import shutil


STABILITY_KEY = "your_own_api_key"  # for API register link, please read README.md


def gen_pic(prompt: str, pic_path: str, stable_key=STABILITY_KEY):
    response = requests.post(
        url=f"https://api.stability.ai/v2beta/stable-image/generate/sd3",
        headers={
            "Authorization": f"Bearer {stable_key}",
            "accept": "image/*"
        },
        files={
            "none": ''
        },
        data={
            "prompt": f"{prompt}",
            "output_format": "jpeg"
        }
    )
    if response.status_code == 200:
        with open(f"./{pic_path}.jpeg", 'wb') as file:
            file.write(response.content)
    else:
        raise Exception(str(response.json()))
    return


# Preparations
df = pd.read_excel(r"/content/correct_image_reference.xlsx")  # the Excel file in this repository
fig_path_prefix = r"/Scientific_graphs"
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
        fig_path = join(fig_path_prefix, key) + "_0"
        gen_pic(prompt_prefix + val, fig_path)

# Image package and download
folder_path = '/content/Scientific_graphs'
output_filename = '/content/scientific_graphs'
shutil.make_archive(output_filename, 'zip', folder_path)
print("All file downloaded")
