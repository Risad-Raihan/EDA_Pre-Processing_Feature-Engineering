
# To observe missing values percentage of every feature in the data set

features_with_na =[features for features in dateset.columns if dateset[features].isnull().sum()>1]

for feature in features_with_na:
  print(feature, np.round(dateset[feature].isnull().mean(), 4), ' % missing values')


