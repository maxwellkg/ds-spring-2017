#!pip install pyshp
# %load read_shapefile.py
import shapefile
import pickle
import pandas as pd

#Read in the shapefile, extract important features
sf = shapefile.Reader('ZillowNeighborhoods-NY/ZillowNeighborhoods-NY')
shapes = sf.shapes()
records = sf.records()
fields = sf.fields

#Create column name array
columns = []

for i in range(1,6):
    columns.append(fields[i][0])

#Create dictionary of latitude and longitude for each neighborhood
bbox = []
bdat = {'bllong':[],'bllat':[],'trlong':[],'trlat':[]}
for item in shapes:
    bbox.append(item.bbox)
for item in bbox:
    bdat['bllong'].append(item[0])
    bdat['bllat'].append(item[1])
    bdat['trlong'].append(item[2])
    bdat['trlat'].append(item[3])

#Convert dictionary to dataframe and add in column names, neighborhood names
nb_frame = pd.DataFrame(records,columns=columns)
nb_frame['bllong'] = bdat['bllong']
nb_frame['bllat'] = bdat['bllat']
nb_frame['trlong'] = bdat['trlong']
nb_frame['trlat'] = bdat['trlat']
nynb_frame = nb_frame.loc[nb_frame['City']=='New York']
use_frame = nynb_frame.filter(items=['Name','bllong','bllat','trlong','trlat'],axis=1)

#Pickle data
use_frame.to_pickle('neighborhoods.p')