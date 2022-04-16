import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("data1.csv")


cols = ['BikingOrdinalScaleNum', "BoatingOrdinalScaleNum", "CampingOrdinalScaleNum", "FishingOrdinalScaleNum", "GardeningOrdinalScaleNum", "GatheringOrdinalScaleNum", "HikingOrdinalScaleNum", "HuntingOrdinalScaleNum", "JoggingOrdinalScaleNum", "PhotographyOrdinalScaleNum", "RelaxOthersOrdinalScaleNum", "RelaxMyselfOrdinalScaleNum", "RockClimbingOrdinalScaleNum", "WalkingOrdinalScaleNum", "WildlifeOrdinalScaleNum"]
print(len(data["BikingOrdinalScaleNum"].dropna()))