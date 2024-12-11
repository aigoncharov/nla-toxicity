from prompt_source import get_prompts
from domain_pairs import generate_domain_pairs
import json
from datetime import datetime

prompts = get_prompts()
print(len(prompts))

file_name = f"clickbait_pairwise_{datetime.now().strftime('%Y-%m-%d-%H_%M_%S')}.jsonl"

for i, prompt in enumerate(prompts):
    print(f"Generating {i + 1} out of {len(prompts)}")
    gold, unpert, pert = generate_domain_pairs(prompt)
    res = {"prompt_text": prompt, "gold_text": gold[0], "unpert_gen_text": unpert[0], "pert_gen_text": pert[0]}
    with open(file_name, "a") as out:
        out.write(json.dumps(res))
        out.write("\n")

print("===DONE===")
