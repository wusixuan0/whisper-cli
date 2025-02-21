import json

def load_json_file(file_path):
    """Loads a JSON object from a file."""
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

def save_json_file(data, file_path, indent=4):
    """Saves a JSON object to a file."""
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=indent)
    print(f"Saved to {file_path}")

def extract_recent_conversation(file_path):
    data = load_json_file(file_path)
    data = [chat for chat in data if (chat['created_at'] <= '2025-02-14' and chat['created_at'] > '2025-02-09')]

    new_file_path = file_path.replace(".json", "_recent.json")
    save_json_file(data, new_file_path)
    


if __name__ == '__main__':
    file_path = '/Users/sixuan/Downloads/claude-history-25-02-15/conversations.json'
    extract_recent_conversation(file_path)

