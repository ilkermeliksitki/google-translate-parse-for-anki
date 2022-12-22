#!/usr/bin/env python3
import pandas as pd
import csv
import time

df = pd.read_csv("~/Downloads/Saved translations - Saved translations.csv")
df.columns = ["lang1", "lang2", "def1", "def2"]

en_tr = df[(df["lang1"] == "English") & (df["lang2"] == "Turkish")]
en_de = df[(df["lang1"] == "English") & (df["lang2"] == "German")]
de_en = df[(df["lang1"] == "German") & (df["lang2"] == "English")]
de_tr = df[(df["lang1"] == "German") & (df["lang2"] == "Turkish")]
tr_en = df[(df["lang1"] == "Turkish") & (df["lang2"] == "English")]
tr_de = df[(df["lang1"] == "Turkish") & (df["lang2"] == "German")]


en_tr.to_csv("~/Desktop/en-tr.csv", index=False, header=False)
#print(en_de)
en_de.to_csv("~/Desktop/en-de.csv", index=False, header=False)
#print(de_en)
de_en.to_csv("~/Desktop/de-en.csv", index=False, header=False)
#print(de_tr)
de_tr.to_csv("~/Desktop/de-tr.csv", index=False, header=False)
#print(tr_en)
tr_en.to_csv("~/Desktop/tr-en.csv", index=False, header=False)
#print(tr_de)
tr_de.to_csv("~/Desktop/tr-de.csv", index=False, header=False)

lim = 51 
for i in range(1, lim):
    f = i * '='
    e = (lim - i - 1) * '-'
    print(f"[{f + '>' + e}] {2 * i}%", end='\r')
    time.sleep(0.01)
    if i == lim - 1:
        print()

print("csv files are created at desktop.")
