from datasets import load_dataset

print(f"{'>'*20}[LOADING DATASET]{'<'*20}")
dataset = load_dataset("imagefolder", data_dir="images")
print(f"{'>'*20}[LOADED DATASET]{'<'*20}")

print(dataset)
dataset= dataset.shuffle(seed=45)

# dataset.save_to_disk("MidjourneV6_Image_small")


def push_dataset(dataset):
    try:
        dataset.push_to_hub("ideepankarsharma2003/ImageClassificationStableDiffusion_small_v2")
    except:
        push_dataset(dataset)

push_dataset(dataset)

print(f"{'>'*20}[ALL DONE]{'<'*20}")