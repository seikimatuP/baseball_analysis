#%%
###### maxScherzer.csv
import pandas as pd
import scatterPlotBaseball

read_csv_name = input()
df = pd.read_csv(read_csv_name) 

scatterPlotBaseball.scatter_plot(df)



# %%
import pandas as pd
import numpy as np
from ggplot import *

#df.columns

p=ggplot(df, aes(x='pfx_x',y='pfx_z', colour='pitch_name')) + geom_point()
#+ geom_point(aes(color=pitch_name))
p

# %%
