# utils.py
import json
import os

def save_to_dataset(input_text, translated_text, dataset_path="dataset/dataset.json"):
    # Check if the dataset exists
    if os.path.exists(dataset_path):
        with open(dataset_path, "r") as file:
            dataset = json.load(file)
    else:
        dataset = []
    
    # Check if translation is the same as original (add only when it's different)
    if input_text != translated_text:
        dataset.append({"input": input_text, "translated": translated_text})
    
    # Save the updated dataset
    with open(dataset_path, "w") as file:
        json.dump(dataset, file, indent=4)
