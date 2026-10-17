import pandas as pd
import os, sys, json

def clean(df, cols=[]):
    try:
        for i, row in df.iterrows():
            if row["Age"] > 0:
                if row["Age"] < 100:
                    if row["Gender"] == "Male":
                        df.loc[i, "g"] = 1
                    else:
                        df.loc[i, "g"] = 0
    except:
        pass
    print("done")
    return df
    cols.append("x")