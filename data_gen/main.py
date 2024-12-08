from prompt_source import get_prompts
from domain_pairs import generate_domain_pairs
import json

prompts = get_prompts()
print(len(prompts))

for i, prompt in enumerate(prompts):
    print(f"Generating {i + 1} out of {len(prompts)}")
    gold, unpert, pert = generate_domain_pairs(prompt)
    res = {"prompt_text": prompt, "gold_text": gold[0], "unpert_gen_text": unpert[0], "pert_gen_text": pert[0]}
    with open("sentiment_split.jsonl", "a") as out:
        out.write(json.dumps(res))
        out.write("\n")

print("===DONE===")
