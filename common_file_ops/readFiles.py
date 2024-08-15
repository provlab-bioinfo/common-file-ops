import pandas as pd
import search_tools as st
import numpy as np
import json

def readTabular(path: str, fields: list[str], ids: dict):

        # Read the file
        df = st.importToDataFrame(path)
    
        # Get counts of columns
        baseCols = dict.fromkeys(fields + list(ids.keys()),0)
        colCount = dict(pd.Series(df.columns).value_counts())
        baseCols.update((k, colCount[k]) for k in set(colCount).intersection(baseCols))

        # Check that all columns for fields and IDs exist in data frame and only occur once
        badCols = {col: count for col, count in baseCols.items() if count != 1}
        if (badCols):
            for col, val in badCols.items():
                if val == 0: badCols[col] = "Missing"
                if val > 1: badCols[col] = "Duplicated"
            out = pd.DataFrame.from_dict(badCols, orient='index', columns=['Status:'])
            out = out.reset_index(names=['Column:']).to_string(index=False, col_space = 10, justify = "left")
            print(f"Error reading tabular data. Columns are either missing or duplicated:\nFile: {path}\n{out}")
            raise ValueError(f"Error reading tabular data. Columns are either not present or duplicated:\n   File: {path}\n   Columns:\n{out}")

        # Find all of the samples that meet the ID criteria
        ind = [True] * len(df)
        for col, vals in ids.items():
            ind = ind & (df[col].isin(vals))
        data = df[ind]

        # Return just the fields and ids
        return data[np.unique(list(ids.keys()) + fields)]

def readXML(path: str, fields: list[str], ids: dict):
    blah = 1

def readJSON(path: str, fields: list[str], ids: dict = None): 
    data = json.load(open(path))
    if not isinstance(fields, list): fields = [fields]
    
    def recurseDict(data, fields):
        if isinstance(fields, str):
            return data[fields]
        else:
            key = list(fields.keys())[0]
            return recurseDict(data[key], fields[key])

    out = [recurseDict(data, field) for field in fields]
    if (len(out) == 1): out = out[0]

    return out