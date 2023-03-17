
from openai.embeddings_utils import get_embedding, cosine_similarity
import pandas as pd
import numpy as np

import os
import openai


openai.api_key = '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'
root_path = os.getcwd()


# search through the reviews for a specific product

def search_reviews(search, n=3, pprint=True):
    print(f'search key: {search}')
    datafile_path = f"{root_path}/openai_handle/output/fine_food_reviews_with_embeddings_1k.csv"

    df = pd.read_csv(datafile_path)
    df["embedding"] = df.embedding.apply(eval).apply(np.array)
    product_embedding = get_embedding(
        search,
        engine="text-embedding-ada-002"
    )
    df["similarity"] = df.embedding.apply(
        lambda x: cosine_similarity(x, product_embedding))

    results = (
        df.sort_values("similarity", ascending=False)
        .head(n)
        .combined.str.replace("Title: ", "")
        .str.replace("; Content:", ": ")
    )
    if pprint:
        for r in results:
            print(r[:200])
            print()
    return results

# results = search_reviews(df, "normal rating", n=3)
