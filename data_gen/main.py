from prompt_source import get_prompts
from domain_pairs import generate_domain_pairs

prompts = get_prompts()
print(len(prompts))

print(prompts[0])
res = generate_domain_pairs(prompts[0])
print(res[0])
for it in res[1]:
    print(it)
