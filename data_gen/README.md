# nla-toxicity datagen

## Prerequisites

1. Classifier: [ROBERTA clickbait](https://s3.amazonaws.com/models.huggingface.co/bert/pplm/discriminators/clickbait_classifier_head.pt)
   1. Download https://s3.amazonaws.com/models.huggingface.co/bert/pplm/discriminators/clickbait_classifier_head.pt to `data` folder
2. Prompt source: [Million news](https://huggingface.co/datasets/rajistics/million-headlines/resolve/main/abcnews-date-text_train.csv)
   1. Download https://huggingface.co/datasets/rajistics/million-headlines/resolve/main/abcnews-date-text_train.csv to `data` folder

## Running

1. `poetry install`
2. `poetry run python main.py`