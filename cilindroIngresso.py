import pandas as pd

dfCloud=pd.read_hdf('outputFiles/RANScylLeak2')
mantieni = ['x','y','z','CLOUD','BC','IC','axis','radius']
for col in dfCloud.columns:
    if col not in mantieni:
        dfCloud.drop(columns=col,inplace=True)
dfCloud.to_csv('outputFiles/RANScylLeak2.csv')