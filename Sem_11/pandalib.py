import pandas as pd
df = pd.read_csv('california_housing_train.csv')

# # Самостоятельная практика №1

# print(df)
# print('='*50)
# print(df.shape)
# print('='*50)
# print(df.dtypes)
# print('='*50)
# print(df.isnull().sum())
# print('='*50)


# # Самостоятельная практика №2
# print(df.loc[df['median_income'] < 2, ['median_house_value']])
# print(df.loc[df['median_income'] < 2, ['longitude', 'latitude']])
#
# print(df[(df['housing_median_age'] < 20) &
# #      (df['median_house_value'] > 70000)])


# Самостоятельная практика №3
print(df['median_house_value'].max())
print(df['median_house_value'].min())
print(df.loc[df['median_income'] == 3.1250, ['median_house_value']].max())
print(df.loc[df['median_house_value'] == df['median_house_value'].min(), ['population']].max())
