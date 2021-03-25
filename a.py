#!/usr/bin/python3

import pandas as pd

uri = "/home/jefferson/python/movies.csv"
filmes = pd.read_csv(uri)

print(filmes.head())

colunas = filmes.columns

print(colunas)

filmes.columns = ["filmeId","titulo","generos"]

print(filmes.head())


uri = "/home/jefferson/python/ratings.csv"
notas = pd.read_csv(uri)
notas.head()
notas.columns = ["usuarioId","filmeId","nota","momento"]
print(notas.head())

print(notas["nota"])

print(notas["nota"].unique())

print(notas["nota"].mean())

print(notas["nota"].min())

print(notas["nota"].max())

print(notas.describe())
