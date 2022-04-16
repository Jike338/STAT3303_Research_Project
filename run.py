import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("data.csv")


cols = ['BikingOrdinalScaleNum', "BoatingOrdinalScaleNum", "CampingOrdinalScaleNum", "FishingOrdinalScaleNum", "GardeningOrdinalScaleNum", "GatheringOrdinalScaleNum", "HikingOrdinalScaleNum", "HuntingOrdinalScaleNum", "JoggingOrdinalScaleNum", "PhotographyOrdinalScaleNum", "RelaxOthersOrdinalScaleNum", "RelaxMyselfOrdinalScaleNum", "RockClimbingOrdinalScaleNum", "WalkingOrdinalScaleNum", "WildlifeOrdinalScaleNum"]
df = pd.DataFrame(columns=["Category", "Less", "Same", "More", "Don't Do This Activity"])
for col in cols:
    col_data = data[col].value_counts(normalize=True).sort_index()
    df = df.append([{"Category":col.split("Ordinal")[0], "Less":col_data[1], "Same":col_data[2], "More": col_data[3], "Don't Do This Activity": col_data[0]}])

df.plot(
    x = 'Category',
    kind = 'barh',
    stacked = True,
    title = 'COVID-19 and human-nature relationships: Vermonters’ activities in nature and associated nonmaterial values during the pandemic',
    mark_right = True)
plt.show()
