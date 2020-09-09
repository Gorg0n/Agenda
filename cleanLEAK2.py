import pandas as pd

def calcSW(df,dudx,dudy,dudz,dvdx,dvdy,dvdz,dwdx,dwdy,dwdz):
    df['S']=0.0
    df['W']=0.0

    for ind in df.index:
        row = df.loc[ind]
        a = row[dudx]
        b = row[dudy]
        c = row[dudz]

        d = row[dvdx]
        e = row[dvdy]
        f = row[dvdz]

        g = row[dwdx]
        h = row[dwdy]
        i = row[dwdz]

        A = a
        B = 0.5 * (b + d)
        C = 0.5 * (c + g)

        D = 0.5 * (d + b)
        E = e
        F = 0.5 * (f + h)

        G = 0.5 * (g + c)
        H = 0.5 * (h + f)
        I = i

        S = A**2 + B **2 + C**2 + D**2 +E**2 +F**2 +G**2 +H**2 + I**2
        S = S ** 0.5

        df.at[ind,'S']=S

        B = 0.5 * (b - d)
        C = 0.5 * (c - g)

        D = 0.5 * (d - b)
        F = 0.5 * (f - h)

        G = 0.5 * (g - c)
        H = 0.5 * (h - f)

        W = B **2 + C**2 + D**2 +F**2 +G**2 +H**2
        W = W ** 0.5

        df.at[ind,'W']=W
    return



df = pd.read_csv('inputFiles/URANSleak1.csv', low_memory=False,skiprows=5)
print(df.columns)

df.columns= \
    ['ddd','x','y','z','CH4MF','dCH4MF','nut','dnut','p','dp','T','epsilon','depsilon','k','dk','velocity',
     'dudx','dudy','dudz','dvdx','dvdy','dvdz','dwdx','dwdy','dwdz','WSSx', 'WSSy','WSSz','a','b','c']

print(df.describe())
print(df.shape)
print('dropping stuff')
df.drop(columns=['ddd','WSSy','WSSz','a','b','c'],inplace=True)
print('calculate S and W')
calcSW(df,'dudx','dudy','dudz','dvdx','dvdy','dvdz','dwdx','dwdy','dwdz')
print('dropping stuff again')
df.drop(columns=['dudx','dudy','dudz','dvdx','dvdy','dvdz','dwdx','dwdy','dwdz'],inplace=True)
print(df.columns)

n = 0
df['BC']=0
for ind, el in enumerate(df['WSSx']):
    if el == ' null':
        n += 1
    else:
        df.at[ind,'BC']=1
m = len(df['WSSx']) - n

df2 = pd.DataFrame(df.loc[df['WSSx'] != ' null'])
df2.drop(columns=['WSSx'],inplace=True)
df2.to_csv('outputFiles/boundaryURANSleak2.csv')
df2.to_hdf('outputFiles/boundaryURANSleak2.h5', key='df', mode='w')
print('written boundary file')
df.drop(columns=['WSSx'],inplace=True)
df.to_hdf('outputFiles/URANSleak2clean.h5', key='df', mode='w')
df.to_csv('outputFiles/URANSleak2clean.csv')
print('written csv file')
print(m,n,len(df2))
