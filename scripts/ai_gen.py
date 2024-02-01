import json

urls= json.load(open("research/urls.json"))
from tqdm import tqdm
import requests


i=0


for url in tqdm(urls):
    filename= f"ai_gen_images/image_{i}.png"
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