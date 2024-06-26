import json
from pathlib import Path

file_path = 'data.json'

def save_file(destinations):
    with open(file_path, 'w') as f:  
        json.dump(destinations, f)

# def read_file(in_destinations):
#     in_destinations.clear()
#     if Path(file_path).exists() and Path(file_path).is_file():
#         with open(file_path, 'r') as f:
#             destinations1 = json.load(f)
#             for destination in destinations1:
#                 in_destinations.append(destination)

def read_file():
    if Path(file_path).exists() and Path(file_path).is_file():
        with open(file_path, 'r') as f:
            destinations1 = json.load(f)
            return destinations1
        
    return []