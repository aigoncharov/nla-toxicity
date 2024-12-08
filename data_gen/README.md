# nla-toxicity datagen

## Prerequisites

1. Classifier: [sentiment SST2 ROBERTA](https://s3.amazonaws.com/models.huggingface.co/bert/pplm/discriminators/SST_classifier_head.pt)
   1. Download https://s3.amazonaws.com/models.huggingface.co/bert/pplm/discriminators/SST_classifier_head.pt to `data` folder
2. Prompt source: [Cornell Movie Dialogs Corpus](https://github.com/CornellNLP/ConvoKit/blob/64f40a542a8bbc4a4981cebe17955a59fa5c3812/convokit/util.py#L42)
   1. Download from http://zissou.infosci.cornell.edu/convokit/datasets/movie-corpus/movie-corpus.zip
   2. Unpack to `data` folder

## Running

1. `poetry install`
2. `poetry run python main.py`