from transformers import GPT2LMHeadModel, GPT2Tokenizer
from run_pplm import run_pplm

gpt2_model = GPT2LMHeadModel.from_pretrained("gpt2")
gpt2_tokenizer = GPT2Tokenizer.from_pretrained("gpt2")


def generate_domain_pairs(prompt):
    input_ids = gpt2_tokenizer.encode(prompt, return_tensors="pt")
    normal_output = gpt2_model.generate(input_ids, do_sample=False, max_length=50)
    normal_text = gpt2_tokenizer.decode(normal_output[0], skip_special_tokens=True)

    domain_output = run_pplm(cond_text=prompt)

    return normal_text, domain_output
