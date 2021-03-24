#!/usr/bin/env python
#-*- coding: UTF-8 -*-

import pandas as pd
import unicodedata
path = r"data/data-base-source/QNA_for_bots.csv
data_base = pd.read_csv(path,  sep=";", encoding="latin")
with open("data/faq/faq-nlu.yml", "wt", encoding="utf-8") as f:
    f.write('version: "2.0" \n')
    f.write('\n')
    f.write("nlu:\n")
    for num_pivot in range(1,len(data_base)):
        data_base_pivot = data_base.loc[data_base["id_question_pivot"]==num_pivot,]
        f.write("- intent: faq/" + str(num_pivot) + "\n")
        f.write("  examples: |\n")
        for row in range(len(data_base_pivot)):
            text = str(data_base_pivot.iloc[row,1])
            text = unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore').decode("utf-8")
            f.write(f"   - {text}\n")
        f.write("\n")