import pandas as pd

inFolder = 'inputFiles/'
outFolder = 'outputFiles/'
fileName = 'leakLocation2.csv'

fin = inFolder+fileName
df = pd.read_csv(fin,skiprows=5)
print(df.columns)
df.columns= ['a','x','y','z','b','c','d','e','f','g']
df.drop(columns=['a','b','c','d','e','f','g'],inplace=True)
outFile = outFolder+fileName
df.to_csv(outFile,index=None)

print('ciao')