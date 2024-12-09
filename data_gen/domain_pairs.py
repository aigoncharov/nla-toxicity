from transformers import GPT2LMHeadModel, GPT2Tokenizer
from run_pplm import run_pplm
import torch
import re

LEN = 30

device = "cuda" if torch.cuda.is_available() else "cpu"
# load pretrained model
model = GPT2LMHeadModel.from_pretrained("openai-community/gpt2-medium", output_hidden_states=True)
model.to(device)
model.eval()
# load tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("openai-community/gpt2-medium")


def clean_decoded_text(text: str) -> str:
    """Clean up text decoded from GPT2Tokenizer by removing special tokens and extra whitespace.

    Args:
        text (str): Raw decoded text from tokenizer

    Returns:
        str: Cleaned text
    """
    # Remove special tokens
    text = text.replace("<|endoftext|>", "")

    # Replace multiple newlines with single newline
    text = re.sub(r"\n+", "\n", text)

    # Replace Unicode whitespace characters (including \u00a0) with regular space
    text = re.sub(r"[\u00a0\u1680\u2000-\u200a\u202f\u205f\u3000]", " ", text)

    # Replace multiple spaces with single space
    text = re.sub(r"\s+", " ", text)

    # Remove leading/trailing whitespace (handles both regular and Unicode whitespace)
    text = text.strip()

    # Fix spacing around punctuation
    text = re.sub(r"\s+([,.!?;:])", r"\1", text)

    # Remove any remaining control characters
    text = re.sub(r"[\x00-\x1F\x7F-\x9F]", "", text)

    return text


def generate_domain_pairs(prompt):
    inputs = tokenizer(
        prompt,
        return_tensors="pt",
    )
    gold_tok_text = model.generate(
        input_ids=inputs["input_ids"],
        do_sample=False,
        max_new_tokens=LEN,
    )
    gold_text = tokenizer.decode(gold_tok_text.tolist()[0], skip_special_tokens=True)

    unpert, pert = run_pplm(model, tokenizer, cond_text=prompt, length=LEN)

    return (
        (clean_decoded_text(gold_text), gold_tok_text),
        (clean_decoded_text(unpert[0]), unpert[1]),
        (clean_decoded_text(pert[0]), pert[1]),
    )
