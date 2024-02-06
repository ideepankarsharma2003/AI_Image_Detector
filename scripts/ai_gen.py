import json
import os
urls= json.load(open("outputs/image_playground_ai_imageurls.json"))
from tqdm import tqdm
import requests


i=0

os.makedirs("ai_gen_images", exist_ok=True)


for url in tqdm(urls):
    filename= f"ai_gen_images/pg_ai_image_{i}.JPEG"
    i+=1
    try:
        response= requests.get(url)
        if response.ok:
            with open(filename, "wb") as f:
                f.write(response.content)
        else:
            print("response not ok: ", url)

    except:
        print(url)