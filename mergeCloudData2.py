import pandas as pd
import numpy as np

inFolder = 'outputFiles/'
outFolder = 'outputFiles/'
fileRANS = 'RANSclean.h5'
fileCloud = 'CLOUDcolURANSleak2clean.h5'
fileLeak = 'leakLocation2.csv'
deltax = 0.063
deltay = 0.0
deltaz = 0.0

fin = inFolder + fileRANS
df = pd.read_hdf(fin)
fin = inFolder + fileCloud
dfC = pd.read_hdf(fin)
fin = inFolder + fileLeak
dfLeak = pd.read_csv(fin)


print(df.shape)
print(df.columns)
print(dfC.shape)
print(dfC.columns)
print(dfLeak.shape)
print(dfLeak.columns)

df['CLOUD'] = dfC['CLOUD'].values
df.drop(columns=['CH4MF','dCH4MF'])
xmin = dfLeak['x'].min()-deltax
xmax = dfLeak['x'].max()+deltax
xave = (xmin + xmax )/2
ymin = dfLeak['y'].min()
ymax = dfLeak['y'].max()
yave = (ymin+ymax)/2
zmin = dfLeak['z'].min()
zmax = dfLeak['z'].max()
zave = (zmin + zmax)/2

print(xmin,xmax,ymin,ymax,zmin,zmax)

df['IC']=0
conta=0

for ind in df.index:
    row = df.loc[ind]
    if row['x']< xmax and row['x']>xmin and row['y']<ymax and row['y']>ymin and row['z']<zmax and row['z']>zmin:
        conta +=1
        df.at[ind, 'IC'] = 1

print('numero celle individuate come IC:', conta)

df['axis']= -1* (df['x']-xave)
df['radius'] = np.sqrt((df['y']-yave)**2 + (df['z']-zave)**2)
fin = outFolder+'RANSconLeak2'
df.to_hdf(fin, key='df', mode='w')
dfCloud = pd.DataFrame(df.loc[df['radius'] < 1])
print('cilindro del getto: ', dfCloud.shape)
fin = outFolder+'RANScylLeak2'
dfCloud.to_hdf(fin, key='dfCloud', mode='w')

mantieni = ['x','y','z','CLOUD','BC','IC','axis','radius']
for col in dfCloud.columns:
    if col not in mantieni:
        dfCloud.drop(columns=col,inplace=True)
dfCloud.to_csv('outputFiles/RANScylLeak2.csv')
print('ciao')
