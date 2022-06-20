# %%
import pandas as pd
import datetime

# %%
df = pd.read_excel('https://www.eia.gov/dnav/pet/hist_xls/RBRTEd.xls', sheet_name='Data 1', skiprows=2)

# %%
d = datetime.datetime.now()
today = d.strftime('%Y-%m-%d')

# %%
df.to_csv('./data/file_'+today+'.csv', index=False)


