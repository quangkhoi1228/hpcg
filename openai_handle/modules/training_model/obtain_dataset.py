
# imports
import pandas as pd
import tiktoken

from openai.embeddings_utils import get_embedding
import os
import openai

import time


import os
import sys

root_path = os.getcwd()


openai.api_key = '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'

# embedding model parameters
embedding_model = "text-embedding-ada-002"
embedding_encoding = "cl100k_base"  # this the encoding for text-embedding-ada-002
max_tokens = 8000  # the maximum for text-embedding-ada-002 is 8191


# load & inspect dataset
# to save space, we provide a pre-filtered dataset
input_datapath = f"{root_path}/openai_handle/data/fine_food_reviews_1k.csv"
print(f'input datapath: {input_datapath} ')
df = pd.read_csv(input_datapath, index_col=0)
df = df[["Time", "ProductId", "UserId", "Score", "Summary", "Text"]]
df = df.dropna()
df["combined"] = (
    "Title: " + df.Summary.str.strip() + "; Content: " + df.Text.str.strip()
)
print(df.head(2))


# # subsample to 1k most recent reviews and remove samples that are too long
top_n = 1000
# first cut to first 2k entries, assuming less than half will be filtered out
df = df.sort_values("Time").tail(top_n * 2)
df.drop("Time", axis=1, inplace=True)

encoding = tiktoken.get_encoding(embedding_encoding)
st = time.time()


# omit reviews that are too long to embed
df["n_tokens"] = df.combined.apply(lambda x: len(encoding.encode(x)))
df = df[df.n_tokens <= max_tokens].tail(top_n)
print(len(df))


# Ensure you have your API key set in your environment per the README: https://github.com/openai/openai-python#usage


# This may take a few minutes

df["embedding"] = df.combined.apply(
    lambda x: get_embedding(x, engine=embedding_model))
df.to_csv(
    f"{root_path}/openai_handle/output/fine_food_reviews_with_embeddings_1k.csv")

et = time.time()

elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')
