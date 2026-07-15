import json
import os

def save_json(filename, data):

    filepath = os.path.join("data", filename)

    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            try:
                content = json.load(f)
            except:
                content = []
    else:
        content = []

    content.append(data)

    with open(filepath, "w") as f:
        json.dump(content, f, indent=4)