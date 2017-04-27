# import the necessary packages
import pandas as pd
import pickle

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
  features = row['features']
  for feature in features:
    if feature in dummyized_features:
      data.loc[index, feature] = 1


# count the photos

photo_counts = [len(photo_list) for photo_list in data['photos']]
data['photo_count'] = photo_counts

# week of month (1-4)

weeks = []
for date in data['created']:
  

# finally, save the dataframe as a pickle for future use