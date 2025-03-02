import json

# 讀取 JSONL 格式數據
def load_jsonl(file_path):
    data = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            data.append(json.loads(line))
    return data

# 加載數據
data = load_jsonl("finetuning_training_data_golden.jsonl")
print(json.dumps(data[15], indent=2, ensure_ascii=False))