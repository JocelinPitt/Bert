import ktrain
import numpy as np
import pickle
import pandas as pd
from ktrain import text
from tqdm import tqdm
# Docu https://amaiya.github.io/ktrain/text/index.html#ktrain.text.TransformerEmbedding
# https://github.com/amaiya/ktrain/blob/master/ktrain/text/preprocessor.py
# https://huggingface.co/distilbert-base-cased

# Import distilbert Embedder
Model_name = 'distilbert-base-cased'
Embedder = ktrain.text.TransformerEmbedding(Model_name)

# Import Data
Data = pd.read_csv('Data_essays/essays.csv')

'''# Get posts and matrix Labels
df = Data[['posts', 'type']]
df.reset_index(drop=True, inplace=True)
df = pd.concat([df, df.type.astype('str').str.get_dummies()], axis=1, sort=False)
df.drop('type', axis=1, inplace=True)
df.rename(columns={'posts': 'text'}, inplace=True)

Labels_names = df.columns.values[1:]
labels = df.loc[:, df.columns != 'text']

# Get Liwcs
LIWCs = Data.loc[:, ~Data.columns.isin(['#AUTHID', 'text'])]
print('Setup done \n')'''

#
_temp = list()

for text in tqdm(Data['text'].values.tolist()):
    embd = Embedder.embed(text)
    _temp.append(embd)

pickle.dump(_temp, open('Mairesse_embed.pkl', 'wb'))
print('Done')

#pickle.load(_temp open('embed.pkl, 'rb'))
