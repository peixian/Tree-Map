import pandas as pd
import numpy as np
from ast import literal_eval
from bokeh.plotting import figure, output_file, show

def writeTreeDiameter(data):
    """writes the tree diameter to the treeDiameter.js file"""
    with open("demo/js/treeDiameter.js", "w") as out:
        out.write("var addressPoints = [\n")
        for index, row in data.iterrows():
            out.write("[{},{},{}],\n".format(row["Latitude"], row["Longitude"], row["Diameter at Breast Height (in Feet)"]))
        out.write("];")
        

def writeTreeSpecies(data):
    """writes the tree species and count into species.csv"""
    species = data["Tree Species"].value_counts()
    with open("data/species.csv", "w") as out:
        out.write("species,population\n")
    species.to_csv("data/species.csv", mode="a")

data = pd.read_csv("Trees_Owned_by_the_City_of_Champaign.csv")
data["Diameter"] = (data["Diameter at Breast Height (in Feet)"] - data["Diameter at Breast Height (in Feet)"].min())/(data["Diameter at Breast Height (in Feet)"].max() - data["Diameter at Breast Height (in Feet)"].min())

#sanitize
data["Latitude"] = data.apply(lambda row: literal_eval(row["Location"])[0], axis=1)
data["Longitude"] = data.apply(lambda row: literal_eval(row["Location"])[1], axis=1)
data.drop("Location", axis=1, inplace=True)
#drop whatever the vacant site stuff is
data = data[data["Tree Species"] != "vacant site large"]
data = data[data["Tree Species"] != "vacant site medium"]
#fix stump capitization
data.loc[data["Tree Species"] == "stump", ["Tree Species"]] = "Stump"

treeGroups = data.groupby("Tree Species")
# print(sorted(data["Tree Species"].unique()))
# print(sorted(data["Location Type"].unique()))
# print(type(data["Tree Species"].value_counts()))
# print(data["Tree Species"].value_counts()[0])
# print(list(data["Tree Species"].value_counts().index)[0])

writeTreeSpecies(data)



# print(len(data["Common Name"].unique()))
# print(data[data["Common Name"] == "Amur corktree"])