import json
import os

def load_file(path):
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)

def save_to_file(filename, trails):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(trails, file, ensure_ascii=False, indent=4)
