# nla-toxicity datagen

## Prerequisites

1. Classifier: [NSFW](https://huggingface.co/michellejieli/NSFW_text_classifier)
   1. Download https://huggingface.co/michellejieli/NSFW_text_classifier/blob/main/pytorch_model.bin as nsfw.bin to `data` folder
2. Prompt source: [Cornell Reddit Corpus (small)](https://convokit.cornell.edu/documentation/reddit-small.html)
   1. Download from https://zissou.infosci.cornell.edu/convokit/datasets/subreddit-corpus/reddit-corpus-small.corpus.zip
   2. Unpack to `data` folder

## Running

1. `poetry install`
2. `poetry run python main.py`