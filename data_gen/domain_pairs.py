from transformers import GPT2LMHeadModel


def generate_domain_pairs(prompt, gpt2_model, domain_classifier):
    # Generate normal version (using regular GPT-2)
    normal_output = gpt2_model.generate(prompt, do_sample=False)  # greedy sampling

    # Generate domain-specific version using PPLM
    domain_output = run_pplm(
        model=gpt2_model,
        cond_text=prompt,
        attribute_classifier=domain_classifier,
        # Other PPLM parameters similar to original paper
    )

    return normal_output, domain_output
