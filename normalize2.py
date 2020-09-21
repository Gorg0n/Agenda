import pandas as pd
import numpy as np
from copy import deepcopy
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

inFolder = 'outputFiles/'
outFolder = 'outputFiles/'
fileRANS = 'RANScylLeak2'
fin = inFolder+fileRANS
df = pd.read_hdf(fin)
dfxyz = deepcopy(df[['x','y','z']])
df.drop(columns=['x','y','z','CH4MF','dCH4MF'],inplace=True)

dfNorm = pd.DataFrame()

dontNorm = ['BC', 'CLOUD', 'IC']
for dn in dontNorm:
    dfNorm[dn]=deepcopy(df[dn])

min_max_scaler = MinMaxScaler()
minMaxS = ['T', 'velocity']
for  dn in minMaxS:
    dfNorm[dn] = min_max_scaler.fit_transform(df[[dn]])

print(dfNorm['velocity'].max())
print(dfNorm['velocity'].min())
print(dfNorm['T'].max())
print(dfNorm['T'].min())

#df['LRANS']=4*df['velocity']/(df['S']+1e30)
df['LRANS']=(df['k'] **1.5)/df['epsilon']

scaleLocal = ['nut', 'dnut', 'p', 'dp', 'epsilon', 'depsilon', 'k', 'dk', 'S', 'W', 'axis', 'radius']
scales = ('velocity','LRANS')
scale = [(-1,-1),(-1,0),(-2,0),(-2,1),(-3,1),(-3,2),(-2,0),(-2,1),(-1,1),(-1,1),(0,-1),(0,-1)]
print(dfNorm.shape)
print(df.shape)
for  i,dn in enumerate(scaleLocal):
    dfNorm[dn]=deepcopy(df[dn])
    print(dn,dfNorm[dn].min(),dfNorm[dn].max())
    for j,s in enumerate(scales):
        print(scales[j],scale[i][j],df[s].min(),df[s].max())
        dfNorm[dn] *= df[s] * (df[scales[j]]**scale[i][j])
    print('\n')


print(df.columns)


import seaborn as sns

for col in dfNorm.columns:
    ax = sns.boxplot(x=dfNorm[col])
    fn = outFolder + str(col) + '.png'
    plt.savefig(fn)
    plt.close()

'''
print(dfNorm['axis'].max())
print(dfNorm['axis'].min())
print(dfNorm['radius'].max())
print(dfNorm['radius'].min())
'''
plt.figure(figsize=(7,7))
corrMatrix = dfNorm.corr()
sns.heatmap(corrMatrix,vmin=-1,vmax=1,cmap='bwr')
fn = outFolder + 'cmatrix.png'
plt.tight_layout()
plt.savefig(fn)
plt.close()

print(dfxyz.columns)
print(dfNorm.columns)

dfToT = pd.concat([dfxyz,dfNorm],axis=1)
print(dfToT.columns)
print(dfxyz.shape,dfNorm.shape,dfToT.shape)

fn = outFolder + 'Norm' + fileRANS + '.h5'
print('writing file',fn)
dfNorm.to_hdf(fin, key='dfToT', mode='w')
