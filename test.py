# %% [markdown]
# <a href="https://colab.research.google.com/github/CHesseling/sandbox/blob/main/Untitled57.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# %%
import pandas as pd
import datetime

# %%
df = pd.read_excel('https://www.eia.gov/dnav/pet/hist_xls/RBRTEd.xls', sheet_name='Data 1', skiprows=2)

# %%
d = datetime.datetime.now()
today = d.strftime('%Y-%m-%d')

# %%
df.to_csv('RBRTEd'+today+'.csv', index=False)


