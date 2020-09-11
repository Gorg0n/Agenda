import pandas as pd
import numpy as np

inFolder = 'outputFiles/'
outFolder = 'outputFiles/'
fileRANS = 'RANSclean.h5'
fileCloud = 'CLOUDcolURANSleak2clean.h5'
fileLeak = 'boundaryURANSleak2.h5'

fin = inFolder + fileRANS
df = pd.read_hdf(fin)
fin = inFolder + fileCloud
dfC = pd.read_hdf(fin)
fin = inFolder + fileLeak
dfLeak = pd.read_hdf(fin)


print(df.shape)
print(df.columns)
print(dfC.shape)
print(dfC.columns)
print(dfLeak.shape)
print(dfLeak.columns)

df['CLOUD'] = dfC['CLOUD'].values
df.drop(columns=['CH4MF','dCH4MF'])
xmin = dfLeak['x'].min()-0.063
xmax = dfLeak['x'].max()+0.063
xave = (xmin + xmax )/2
ymin = dfLeak['y'].min()
ymax = dfLeak['y'].max()
zmin = dfLeak['z'].min()
zmax = dfLeak['z'].max()

df['IC']=0
conta=0

for ind in df.index:
    row = df.loc[ind]
    if row['x']< xmax and row['x']>xmin and row['y']<ymax and row['y']>ymin and row['z']<zmax and row['z']>zmin:
        conta +=1
        df.at[ind, 'IC'] = 1

print('numero celle individuate come IC:', conta)

df['axis']= np.abs(df['x']-xave)
df['radius'] = np.sqrt(df['y']**2 + df['z']**2)
fin = outFolder+'RANSconLeak2'
df.to_hdf(fin, key='df', mode='w')
dfCloud = pd.DataFrame(df.loc[df['radius'] > 1])
print('cilindro del getto: ', dfCloud.shape)
fin = outFolder+'RANScylLeak2'
dfCloud.to_hdf(fin, key='df', mode='w')
print('ciao')
