#%%

#投手の投球分析チャートをプロットする
import pandas as pd # ライブラリ pandas をインポート
import matplotlib.pyplot as plt
from pandas import plotting
import numpy as np
from ggplot import *

def scatter_plot(df):
    pitch_names = df.loc[:,["pitch_name"]]
    no_pitch_names = pitch_names.drop_duplicates()

    plt.title("Max Scherzer Pitch Movement")
    plt.xlabel("pfx_x")
    plt.ylabel("pfx_z")
    plt.grid(True)
    #p=ggplot(df, aes(x='pfx_x',y='pfx_z', colour='pitch_name')) + geom_point()
    #p
    for i in range(len(no_pitch_names)):
        no_pitch_name = no_pitch_names.iloc[i,0]
        pfx_x = df.query("pitch_name == @no_pitch_name").loc[:,["pfx_x"]] * 30.48
        pfx_z = df.query("pitch_name == @no_pitch_name").loc[:,["pfx_z"]] * 30.48

        
        plt.scatter(pfx_x, pfx_z)
        plt.style.use('ggplot')


# %%
