import pandas as pd
import pathlib

LINE_COUNT = 500


def get_prompts():
    df = pd.read_csv(pathlib.Path(__file__).parent.joinpath("data/abcnews-date-text_train.csv").resolve())

    headlines = []

    for row in df.itertuples():
        headlines.append(row.headline_text)

        if len(headlines) == LINE_COUNT:
            break

    return headlines
