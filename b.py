#!/usr/bin/python3

import pandas as pd
import numpy as np

uri = "/home/jefferson/python/ratings.csv"

df = pd.read_csv(uri)

print(df.head())

print(df.loc[3])

print(df.loc[3]['movieId'])

df['Total de notas'] = df['rating1'] + df['rating2']

total = df['Total de notas'].sum()

print(total)

print(df['rating1'].value_counts())

uri2 = "/home/jefferson/python/movies.csv"

df2 = pd.read_csv(uri2)

movies = df2['title'].str.upper()

print(movies)

print(movies.value_counts().head(1))

anos = df2['data'].apply(lambda data : data.split('-')[0])

print(anos)

print(df2[(df2['title'] == 'Toy Story')])

