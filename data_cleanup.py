# import the necessary packages
import pandas as pd
import pickle
import datetime
from dateutil import parser

data = pd.read_json('train.json')

# dummyize

dummyized_features = [
  'By Owner',
  'Exclusive',
  'Sublet / Lease-Break',
  'No Fee',
  'Reduced Fee',
  'Short Term Allowed',
  'Furnished',
  'Laundry In Unit',
  'Private Outdoor Space',
  'Parking Space',
  'Cats Allowed',
  'Dogs Allowed',
  'Doorman',
  'Elevator',
  'Fitness Center',
  'Laundry in Building',
  'Common Outdoor Space',
  'Storage Facility'
]

for feature in dummyized_features:
  data[feature] = 0

for index, row in data.iterrows():
  for feature in row['features']
    if feature in dummyized_features:
      data.loc[index, feature] = 1

data.drop()


# count the photos
data['photo_count'] = [len(photo_list) for photo_list in data['photos']]

# week of month (1-5)

weeks = []
for create_date in data['created']:
  weeks.append((parser.parse(create_date).day - 1) // 7 + 1)

data['week'] = weeks

# finally, save the dataframe as a pickle for future use

data.to_pickle('pickled_data.p')