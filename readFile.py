import pandas as pd

df = pd.read_hdf('outputFiles/RANSclean.h5')
print(df.shape)
print(df['CH4MF'].max())
print(df['CH4MF'].min())
print(df['dCH4MF'].max())
print(df['dCH4MF'].min())
conta = 0
for ind,b in enumerate(df['CH4MF']):
    if df['CH4MF'].iloc[ind] == 0:
        conta += 1

print(conta)

print('ciao')