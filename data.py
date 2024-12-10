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