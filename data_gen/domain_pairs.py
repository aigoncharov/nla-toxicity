from transformers import GPT2LMHeadModel, GPT2Tokenizer
from run_pplm import run_pplm
import torch

LEN = 30

device = "cuda" if torch.cuda.is_available() else "cpu"
# load pretrained model
model = GPT2LMHeadModel.from_pretrained("openai-community/gpt2-medium", output_hidden_states=True)
model.to(device)
model.eval()
# load tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("openai-community/gpt2-medium")


def generate_domain_pairs(prompt):
    inputs = tokenizer(
        prompt,
        return_tensors="pt",
    )
    gold_tok_text = model.generate(
        input_ids=inputs["input_ids"],
        do_sample=False,
        max_length=LEN,
    )
    gold_text = tokenizer.decode(gold_tok_text.tolist()[0], skip_special_tokens=True)

    unpert, pert = run_pplm(model, tokenizer, cond_text=prompt, length=LEN)

    return (gold_text, gold_tok_text), unpert, pert
