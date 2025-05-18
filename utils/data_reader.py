import os
import json


def read_json(file_path):
    full_path = os.path.join(os.path.dirname(__file__), "..", file_path)
    with open(full_path, "r") as f:
        return json.load(f)
