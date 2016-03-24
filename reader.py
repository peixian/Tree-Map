import pandas as pd
import numpy as np
from ast import literal_eval

def writeTreeHeights(data):
    """docstring for writeTreeHeights"""
    with open("treeHeights.js", "w") as out:
        out.write("var addressPoints = [\n")
        for index, row in data.iterrows():
            out.write("[{},{},{}],\n".format(row["Latitude"], row["Longitude"], row["Diameter at Breast Height (in Feet)"]))
        out.write("];")
        

data = pd.read_csv("Trees_Owned_by_the_City_of_Champaign.csv")
data["Diameter at Breast Height (in Feet)"] = (data["Diameter at Breast Height (in Feet)"] - data["Diameter at Breast Height (in Feet)"].min())/(data["Diameter at Breast Height (in Feet)"].max() - data["Diameter at Breast Height (in Feet)"].min())

#sanitize
data["Latitude"] = data.apply(lambda row: literal_eval(row["Location"])[0], axis=1)
data["Longitude"] = data.apply(lambda row: literal_eval(row["Location"])[1], axis=1)
data.drop("Location", axis=1, inplace=True)

writeTreeHeights(data)