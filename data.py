import pandas as pd    
import json

train_df = pd.read_csv('Customer-Support.csv')
# valid_df = load valid df

# +
import csv
import json

def csv_to_jsonl(csv_file_path, jsonl_file_path):
    """
    Converts a CSV file to a JSONL file.
    import pandas as pd    
import json

train_df = pd.read_csv('GenAI_Program_FAQ_dataset.csv')
# valid_df = load valid df

# Convert the dataset to JSONL format
output_file = 'training.jsonl'
with open(output_file, 'w') as f:
    for _, row in train_df.iterrows():
        # Create JSON lines for chat model fine-tuning
        json_line = json.dumps({
            "messages": [
                {"role": "system", "content": "You are a helpful assistant which acts as FAQ Support Assistant for the TMLC Guided Projects in Generative AI Program and answer to user queries."},
                {"role": "user", "content": row['prompt']},
                {"role": "assistant", "content": row['completion']}
            ]
        })
        f.write(json_line + '\n')

# output_file = 'validation.jsonl'
# with open(output_file, 'w') as f:
#     for _, row in valid_df.iterrows():
#         # Create JSON lines for chat model fine-tuning
#         json_line = json.dumps({
#             "messages": [
#                 {"role": "system", "content": "You are a helpful assistant which acts as Customer Support Associate and answers to user queries."},
#                 {"role": "user", "content": row['prompt']},
#                 {"role": "assistant", "content": row['completion']}
#             ]
#         })
#         f.write(json_line + '\n')

print(f"Dataset converted and saved to {output_file}")
    :param csv_file_path: Path to the input CSV file
    :param jsonl_file_path: Path to the output JSONL file
    """
    try:
        with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            with open(jsonl_file_path, mode='w', encoding='utf-8') as jsonl_file:
                for row in reader:
                    jsonl_file.write(json.dumps(row) + '\n')
        print(f"Successfully converted {csv_file_path} to {jsonl_file_path}.")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
csv_file_path = 'Customer-Support.csv'  # Replace with your CSV file path
jsonl_file_path = 'data.jsonl'  # Replace with your desired JSONL file path
csv_to_jsonl(csv_file_path, jsonl_file_path)
# -

# Convert the dataset to JSONL format
output_file = 'training.jsonl'
with open(output_file, 'w') as f:
    for _, row in train_df.iterrows():
        # Create JSON lines for chat model fine-tuning
        json_line = json.dumps({
            "messages": [
                {"role": "system", "content": "You are a helpful assistant which acts as FAQ Support Assistant for the TMLC Guided Projects in Generative AI Program and answer to user queries."},
                {"role": "user", "content": row['prompt']},
                {"role": "assistant", "content": row['completion']}
            ]
        })
        f.write(json_line + '\n')

# output_file = 'validation.jsonl'
# with open(output_file, 'w') as f:
#     for _, row in valid_df.iterrows():
#         # Create JSON lines for chat model fine-tuning
#         json_line = json.dumps({
#             "messages": [
#                 {"role": "system", "content": "You are a helpful assistant which acts as Customer Support Associate and answers to user queries."},
#                 {"role": "user", "content": row['prompt']},
#                 {"role": "assistant", "content": row['completion']}
#             ]
#         })
#         f.write(json_line + '\n')

# +
import json

# File paths
input_file = 'fixed_file.jsonl'
output_file = 'fixed_file2.jsonl'

# Open the input and output files
with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
    for line in infile:
        # Load the JSON object from the line
        data = json.loads(line)
        
        # Change keys: 'query' -> 'prompt' and 'response' -> 'completion'
        if 'query' in data and 'response' in data:
            data['prompt'] = data.pop('query')
            data['completion'] = data.pop('response')
        
        # Write the modified data to the output file
        json.dump(data, outfile, ensure_ascii=False)
        outfile.write('\n')  # Ensure it's written in JSONL format

# +
import json

input_file = "data.jsonl"
output_file = "fixed_file.jsonl"

# Read and fix the JSON file
with open(input_file, "r") as infile:
    # Read each line as a JSON object
    data = [json.loads(line) for line in infile]

# Save the fixed JSON as an array
with open(output_file, "w") as outfile:
    json.dump(data, outfile, indent=4)

print(f"Fixed JSON saved to {output_file}")

# +
import json

input_file = "fixed_file.jsonl"
output_file = "chat_format.jsonl"

# Load the JSON file
with open(input_file, "r") as infile:
    data = json.load(infile)

# Convert to chat format with error handling
chat_data = []
for item in data:
    try:
        # Adjust keys here if they differ
        prompt = item["prompt"]  # Or item["question"]
        completion = item["completion"]  # Or item["answer"]

        chat_data.append({
            "messages": [
                {"role": "user", "content": prompt},
                {"role": "assistant", "content": completion.strip()}
            ]
        })
    except KeyError as e:
        print(f"Skipping item due to missing key: {e}")

# Save the chat-formatted data
with open(output_file, "w") as outfile:
    json.dump(chat_data, outfile, indent=4)

print(f"Converted data saved to {output_file}")

# +
import json

# Load the prompt-completion file
input_file = "fixed_file.jsonl"
output_file = "chat_format.json"

with open(input_file, "r", encoding='utf-8') as infile:
    data = json.load(infile)

# Convert to chat format
chat_data = []
for item in data:
    chat_data.append({
        "messages": [
            {"role": "user", "content": item["prompt"]},
            {"role": "assistant", "content": item["completion"].strip()}
        ]
    })

# Save the chat-formatted data
with open(output_file, "w") as outfile:
    json.dump(chat_data, outfile, indent=4)

print(f"Converted data saved to {output_file}")
# -


