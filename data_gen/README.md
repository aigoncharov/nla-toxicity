# nla-toxicity datagen

## Prerequisites

1. Classifier: [ROBERTA clickbait](https://s3.amazonaws.com/models.huggingface.co/bert/pplm/discriminators/clickbait_classifier_head.pt)
   1. Download https://s3.amazonaws.com/models.huggingface.co/bert/pplm/discriminators/clickbait_classifier_head.pt to `data` folder
2. Prompt source: [Cornell Reddit Corpus (small)](https://convokit.cornell.edu/documentation/reddit-small.html)
   1. Download from https://zissou.infosci.cornell.edu/convokit/datasets/subreddit-corpus/reddit-corpus-small.corpus.zip
   2. Unpack to `data` folder

## Running

1. `poetry install`
2. `poetry run python main.py`