
# To observe missing values percentage of every feature in the data set

features_with_na =[features for features in dateset.columns if dateset[features].isnull().sum()>1]

for feature in features_with_na:
  print(feature, np.round(dateset[feature].isnull().mean(), 4), ' % missing values')

# Here we need to see if the features of the null value are important or not and compare it with another feature like SalesPrice. It actually indicated and tell us whether we need 
# to drop the null value from the data set or not and replace it 

for feature in features_with_na:
    data = dataset.copy()
    
    # let's make a variable that indicates 1 if the observation was missing or zero otherwise
    data[feature] = np.where(data[feature].isnull(), 1, 0)
    
    # let's calculate the mean SalePrice where the information is missing or present
    data.groupby(feature)['SalePrice'].median().plot.bar()
    plt.title(feature)
    plt.show()

    
