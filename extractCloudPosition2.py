import pandas as pd

inFolder = 'outputFiles/'
outFolder = 'outputFiles/'
fileName = 'URANSleak2clean.h5'

fin = inFolder+fileName

df=pd.read_hdf(fin)

df['CLOUD']=0
conta = 0
for ind, el in enumerate(df['CH4MF']):
    if el > 0.044 and el < 0.15:
        df.at[ind,'CLOUD']=1
        conta +=1
print(df.columns)
print(conta)
dfCloud = df[['x','y','z','CLOUD']].copy()
dfC = df[['CLOUD']].copy()
fin = outFolder+'CLOUDcol'+fileName
dfC.to_hdf(fin, key='dfC', mode='w')
dfCloud = pd.DataFrame(dfCloud.loc[dfCloud['CLOUD'] > 0.5])
print(dfCloud.columns)
fin = outFolder+'CLOUD'+fileName
dfCloud.to_hdf(fin, key='dfCloud', mode='w')
fin = fin+'.csv'
dfCloud.to_csv(fin)
print('ciao')