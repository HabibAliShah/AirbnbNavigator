import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd
import contextily as ctx


# reading Dataset CSV file
data = pd.read_csv('data/listings_melbourne.csv')
data.head() # to get a glimpse of the data
data.shape  # to understand the shape of the data -> returns a tuple representing the dimension

list(data.columns) # to extract the column names

# calculating rental price stats
rental_price = data.loc[:, 'price']

mean_rent = np.mean(rental_price) # on avg, rental price amount
print('Melbourne: The avg rental price is: $', round(mean_rent, 2))

max_rent = np.max(rental_price) # highest rental price
print('Melbourne: The max rental price is: $', round(max_rent, 2))

min_rent = np.min(rental_price) # min rental price
print('Melbourne: The min rental price is: $', round(min_rent, 2))

rent_std = np.std(rental_price) # variation in rental price -> cheap/high
print('Melbourne: The std deviation of rental price is: $', round(rent_std, 2))

median_rent = np.median(rental_price) # half of rentals cost less than this amount and other half cost more
print('Melbourne: The median rental price is: $', round(median_rent, 2))


# Counting unique values
unique_regions_count = data['neighbourhood_group'].value_counts().count() # value_counts() counts occurance of each unique value

# Calculating the percentage of properties by region
percent_by_region = round(data['neighbourhood_group'].value_counts(normalize=True) * 100, 2)
percent_by_region


print(f'There are {data.id.nunique()} unique listings in the neighbourhood\n')

## Check the distribution of price:
plt.figure(figsize=(10, 6))
sns.histplot(data[data['price'] <= 800], x='price', binwidth=50, kde=False, color='blue')
plt.title('Distribution of Rental Prices- Melbourne')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.xticks(np.arange(0, 801, 50))
plt.show()

print('Melbourne: Segmenting distrubtion of price further by room type')
print(data.groupby('room_type')['price'].median())


geometry = gpd.points_from_xy(data['longitude'], data['latitude'])

# Creating GeoDataFrame
gdf = gpd.GeoDataFrame(data, geometry=geometry)

# (CRS) - EPSG:3857 is common for web maps
gdf.crs = 'EPSG:4326'  # assuming your data is in WGS84

# Reproject the data to the Web Mercator projection (meters)
gdf = gdf.to_crs(epsg=3857)

# Create a Matplotlib figure and axis
fig, ax = plt.subplots(1, figsize=(10, 10))

# Plot the points using a color scale based on price
gdf.plot(ax=ax, column='price', cmap='viridis', markersize=5, legend=True)

# Adding a basemap using Contextily
ctx.add_basemap(ax, crs=gdf.crs.to_string(), source=ctx.providers.OpenStreetMap.Mapnik)

plt.title('Melbourne- Listings with Price Color Scale')

plt.show()


# Filter listings with a minimum stay of a week or longer
week_or_longer = data[data['minimum_nights'] >= 7]

# Filter listings without a minimum stay of a week or longer
less_than_week = data[data['minimum_nights'] < 7]

plt.figure(figsize=(8, 8))
sns.histplot(week_or_longer['price'], bins=50, kde=True, color='blue', label='Week or longer')
sns.histplot(less_than_week['price'], bins=50, kde=True, color='red', label='Less than a week')
plt.title("Melbourne- Distribution of price by minimum stay")
plt.legend()
plt.show()

# separate DataFrames for listings with and without a minimum stay of a week or longer
min_stay_week = data[data['minimum_nights'] >= 7]  # min stay of a week or longer
no_min_stay_week = data[data['minimum_nights'] < 7]  # without a min stay of a week or longer

# Compare average price between the two groups
avg_price_min_stay_week = min_stay_week['price'].mean()
avg_price_no_min_stay_week = no_min_stay_week['price'].mean()
print(f"\nMelbourne: Average price for listings with minimum stay of a week or longer: ${avg_price_min_stay_week:.2f}")
print(f"Melbourne: Average price for listings without minimum stay of a week or longer: ${avg_price_no_min_stay_week:.2f} \n")

# **** End for Airbnb Melbourne Data Set ****



# **** Start for Airbnb Austin's Data Set ****


data2 = pd.read_csv('data/listings_austin.csv')
list(data2.columns)

rental_price = data2.loc[:, 'price']

mean_rent = np.mean(rental_price) # on avg, rental price amount
print('Austin: The avg rental price is: $', round(mean_rent, 2))

max_rent = np.max(rental_price) # highest rental price
print('Austin: The max rental price is: $', round(max_rent, 2))

min_rent = np.min(rental_price) # min rental price
print('Austin: The min rental price is: $', round(min_rent, 2))

rent_std = np.std(rental_price) # variation in rental price -> cheap/high
print('Austin: The std deviation of rental price is: $', round(rent_std, 2))

median_rent = np.median(rental_price)
print('Austin: The median rental price is: $', round(median_rent, 2),'\n')

# Check the distribution of price:
plt.figure(figsize=(10, 6))
sns.histplot(data2[data2['price'] <= 800], x='price', binwidth=50, kde=False, color='blue')
plt.title('Austin: Distribution of Rental Prices')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.xticks(np.arange(0, 801, 50))
plt.show()

print('Austin: Segmenting distrubtion of price further by room type')
print(data2.groupby('room_type')['price'].median())

# Map
geometry = gpd.points_from_xy(data2['longitude'], data2['latitude'])

gdf = gpd.GeoDataFrame(data2, geometry=geometry)
gdf.crs = 'EPSG:4326'
gdf = gdf.to_crs(epsg=3857)
fig, ax = plt.subplots(1, figsize=(10, 10))

# Ploting the points
gdf.plot(ax=ax, column='price', cmap='viridis', markersize=5, legend=True)
ctx.add_basemap(ax, crs=gdf.crs.to_string(), source=ctx.providers.OpenStreetMap.Mapnik)
plt.title('Austin- Listings with Price Color Scale')
plt.show()

# Filter listings with a minimum stay of a week or longer
week_or_longer = data2[data2['minimum_nights'] >= 7]

# Filter listings without a minimum stay of a week or longer
less_than_week = data2[data2['minimum_nights'] < 7]

plt.figure(figsize=(8, 8))
sns.histplot(week_or_longer['price'], bins=50, kde=True, color='blue', label='Week or longer')
sns.histplot(less_than_week['price'], bins=50, kde=True, color='red', label='Less than a week')
plt.title("Austin: Distribution of price by minimum stay")
plt.legend()
plt.show()

min_stay_week = data2[data2['minimum_nights'] >= 7]
no_min_stay_week = data2[data2['minimum_nights'] < 7]

avg_price_min_stay_week = min_stay_week['price'].mean()
avg_price_no_min_stay_week = no_min_stay_week['price'].mean()
print(f"\nAustin: Average price for listings with minimum stay of a week or longer: ${avg_price_min_stay_week:.2f}")
print(f"Austin: Average price for listings without minimum stay of a week or longer: ${avg_price_no_min_stay_week:.2f}", '\n')


# **** End for Airbnb Austin's Data Set ****




# **** Start for Airbnb Bankok's Data Set ****


data3 = pd.read_csv('data/listings_bangkok.csv')
list(data3.columns)

rental_price = data3.loc[:, 'price']

mean_rent = np.mean(rental_price) # on avg, rental price amount
print('Bangkok: The avg rental price is: $', round(mean_rent, 2))

max_rent = np.max(rental_price) # highest rental price
print('Bangkok: The max rental price is: $', round(max_rent, 2))

min_rent = np.min(rental_price) # min rental price
print('Bangkok: The min rental price is: $', round(min_rent, 2))

rent_std = np.std(rental_price) # variation in rental price -> cheap/high
print('Bangkok: The std deviation of rental price is: $', round(rent_std, 2))

median_rent = np.median(rental_price)
print('Bangkok: The median rental price is: $', round(median_rent, 2),'\n')

# Check the distribution of price:
plt.figure(figsize=(10, 6))
sns.histplot(data3[data3['price'] <= 800], x='price', binwidth=50, kde=False, color='blue')
plt.title('Bangkok: Distribution of Rental Prices')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.xticks(np.arange(0, 801, 50))
plt.show()

print('Bangkok: Segmenting distribution of price further by room type')
print(data3.groupby('room_type')['price'].median())

# Map
geometry = gpd.points_from_xy(data3['longitude'], data3['latitude'])

gdf = gpd.GeoDataFrame(data3, geometry=geometry)
gdf.crs = 'EPSG:4326'
gdf = gdf.to_crs(epsg=3857)
fig, ax = plt.subplots(1, figsize=(10, 10))

# Ploting the points
gdf.plot(ax=ax, column='price', cmap='viridis', markersize=5, legend=True)
ctx.add_basemap(ax, crs=gdf.crs.to_string(), source=ctx.providers.OpenStreetMap.Mapnik)
plt.title('Bangkok- Listings with Price Color Scale')
plt.show()

# Filter listings with a minimum stay of a week or longer
week_or_longer = data3[data3['minimum_nights'] >= 7]

# Filter listings without a minimum stay of a week or longer
less_than_week = data3[data3['minimum_nights'] < 7]

plt.figure(figsize=(8, 8))
sns.histplot(week_or_longer['price'], bins=50, kde=True, color='blue', label='Week or longer')
sns.histplot(less_than_week['price'], bins=50, kde=True, color='red', label='Less than a week')
plt.title("Bangkok: Distribution of price by minimum stay")
plt.legend()
plt.show()

min_stay_week = data3[data3['minimum_nights'] >= 7]
no_min_stay_week = data3[data3['minimum_nights'] < 7]

avg_price_min_stay_week = min_stay_week['price'].mean()
avg_price_no_min_stay_week = no_min_stay_week['price'].mean()
print(f"\nBangkok: Average price for listings with minimum stay of a week or longer: ${avg_price_min_stay_week:.2f}")
print(f"Bangkok: Average price for listings without minimum stay of a week or longer: ${avg_price_no_min_stay_week:.2f}", '\n')


# **** End for Airbnb Bankok's Data Set ****




# **** Start for Airbnb Buenos Aires's Data Set ****


data4 = pd.read_csv('data/listings_buenos_aires.csv')
list(data4.columns)

rental_price = data4.loc[:, 'price']

mean_rent = np.mean(rental_price) # on avg, rental price amount
print('Buenos Aires: The avg rental price is: $', round(mean_rent, 2))

max_rent = np.max(rental_price) # highest rental price
print('Buenos Aires: The max rental price is: $', round(max_rent, 2))

min_rent = np.min(rental_price) # min rental price
print('Buenos Aires: The min rental price is: $', round(min_rent, 2))

rent_std = np.std(rental_price) # variation in rental price -> cheap/high
print('Buenos Aires: The std deviation of rental price is: $', round(rent_std, 2))

median_rent = np.median(rental_price)
print('Buenos Aires: The median rental price is: $', round(median_rent, 2),'\n')

# Check the distribution of price:
plt.figure(figsize=(10, 6))
sns.histplot(data4[data4['price'] <= 800], x='price', binwidth=50, kde=False, color='blue')
plt.title('Buenos Aires: Distribution of Rental Prices')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.xticks(np.arange(0, 801, 50))
plt.show()

print('Buenos Aires: Segmenting distribution of price further by room type')
print(data4.groupby('room_type')['price'].median())

# Map
geometry = gpd.points_from_xy(data4['longitude'], data4['latitude'])

gdf = gpd.GeoDataFrame(data4, geometry=geometry)
gdf.crs = 'EPSG:4326'
gdf = gdf.to_crs(epsg=3857)
fig, ax = plt.subplots(1, figsize=(10, 10))

# Ploting the points
gdf.plot(ax=ax, column='price', cmap='viridis', markersize=5, legend=True)
ctx.add_basemap(ax, crs=gdf.crs.to_string(), source=ctx.providers.OpenStreetMap.Mapnik)
plt.title('Buenos Aires- Listings with Price Color Scale')
plt.show()

# Filter listings with a minimum stay of a week or longer
week_or_longer = data4[data4['minimum_nights'] >= 7]

# Filter listings without a minimum stay of a week or longer
less_than_week = data4[data4['minimum_nights'] < 7]

plt.figure(figsize=(8, 8))
sns.histplot(week_or_longer['price'], bins=50, kde=True, color='blue', label='Week or longer')
sns.histplot(less_than_week['price'], bins=50, kde=True, color='red', label='Less than a week')
plt.title("Buenos Aires: Distribution of price by minimum stay")
plt.legend()
plt.show()

min_stay_week = data4[data4['minimum_nights'] >= 7]
no_min_stay_week = data4[data4['minimum_nights'] < 7]

avg_price_min_stay_week = min_stay_week['price'].mean()
avg_price_no_min_stay_week = no_min_stay_week['price'].mean()
print(f"\nBuenos Aires: Average price for listings with minimum stay of a week or longer: ${avg_price_min_stay_week:.2f}")
print(f"Buenos Aires: Average price for listings without minimum stay of a week or longer: ${avg_price_no_min_stay_week:.2f}", '\n')


# **** End for Airbnb Buenos Aires's Data Set ****



# **** Start for Cape Town Aires's Data Set ****


data5 = pd.read_csv('data/listings_cape_town.csv')
list(data5.columns)

rental_price = data5.loc[:, 'price']

mean_rent = np.mean(rental_price) # on avg, rental price amount
print('Cape Town: The avg rental price is: $', round(mean_rent, 2))

max_rent = np.max(rental_price) # highest rental price
print('Cape Town: The max rental price is: $', round(max_rent, 2))

min_rent = np.min(rental_price) # min rental price
print('Cape Town: The min rental price is: $', round(min_rent, 2))

rent_std = np.std(rental_price) # variation in rental price -> cheap/high
print('Cape Town: The std deviation of rental price is: $', round(rent_std, 2))

median_rent = np.median(rental_price)
print('Cape Town: The median rental price is: $', round(median_rent, 2),'\n')

# Check the distribution of price:
plt.figure(figsize=(10, 6))
sns.histplot(data5[data5['price'] <= 800], x='price', binwidth=50, kde=False, color='blue')
plt.title('Cape Town: Distribution of Rental Prices')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.xticks(np.arange(0, 801, 50))
plt.show()

print('Cape Town: Segmenting distribution of price further by room type')
print(data5.groupby('room_type')['price'].median())

# Map
geometry = gpd.points_from_xy(data5['longitude'], data5['latitude'])

gdf = gpd.GeoDataFrame(data5, geometry=geometry)
gdf.crs = 'EPSG:4326'
gdf = gdf.to_crs(epsg=3857)
fig, ax = plt.subplots(1, figsize=(10, 10))

# Ploting the points
gdf.plot(ax=ax, column='price', cmap='viridis', markersize=5, legend=True)
ctx.add_basemap(ax, crs=gdf.crs.to_string(), source=ctx.providers.OpenStreetMap.Mapnik)
plt.title('Cape Town- Listings with Price Color Scale')
plt.show()

# Filter listings with a minimum stay of a week or longer
week_or_longer = data5[data5['minimum_nights'] >= 7]

# Filter listings without a minimum stay of a week or longer
less_than_week = data5[data5['minimum_nights'] < 7]

plt.figure(figsize=(8, 8))
sns.histplot(week_or_longer['price'], bins=50, kde=True, color='blue', label='Week or longer')
sns.histplot(less_than_week['price'], bins=50, kde=True, color='red', label='Less than a week')
plt.title("Cape Town: Distribution of price by minimum stay")
plt.legend()
plt.show()

min_stay_week = data5[data5['minimum_nights'] >= 7]
no_min_stay_week = data5[data5['minimum_nights'] < 7]

avg_price_min_stay_week = min_stay_week['price'].mean()
avg_price_no_min_stay_week = no_min_stay_week['price'].mean()
print(f"\nCape Town: Average price for listings with minimum stay of a week or longer: ${avg_price_min_stay_week:.2f}", '\n')


# **** End for Airbnb Cape Town's Data Set ****






# **** Start for Istanbul's Data Set ****


data6 = pd.read_csv('data/listings_istanbul.csv')
list(data6.columns)

rental_price = data6.loc[:, 'price']

mean_rent = np.mean(rental_price) # on avg, rental price amount
print('Istanbul: The avg rental price is: $', round(mean_rent, 2))

max_rent = np.max(rental_price) # highest rental price
print('Istanbul: The max rental price is: $', round(max_rent, 2))

min_rent = np.min(rental_price) # min rental price
print('Istanbul: The min rental price is: $', round(min_rent, 2))

rent_std = np.std(rental_price) # variation in rental price -> cheap/high
print('Istanbul: The std deviation of rental price is: $', round(rent_std, 2))

median_rent = np.median(rental_price)
print('Istanbul: The median rental price is: $', round(median_rent, 2),'\n')

# Check the distribution of price:
plt.figure(figsize=(10, 6))
sns.histplot(data6[data6['price'] <= 800], x='price', binwidth=50, kde=False, color='blue')
plt.title('Istanbul: Distribution of Rental Prices')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.xticks(np.arange(0, 801, 50))
plt.show()

print('Istanbul: Segmenting distribution of price further by room type')
print(data6.groupby('room_type')['price'].median())

# Map
geometry = gpd.points_from_xy(data6['longitude'], data6['latitude'])

gdf = gpd.GeoDataFrame(data6, geometry=geometry)
gdf.crs = 'EPSG:4326'
gdf = gdf.to_crs(epsg=3857)
fig, ax = plt.subplots(1, figsize=(10, 10))

# Ploting the points
gdf.plot(ax=ax, column='price', cmap='viridis', markersize=5, legend=True)
ctx.add_basemap(ax, crs=gdf.crs.to_string(), source=ctx.providers.OpenStreetMap.Mapnik)
plt.title('Istanbul- Listings with Price Color Scale')
plt.show()

# Filter listings with a minimum stay of a week or longer
week_or_longer = data6[data6['minimum_nights'] >= 7]

# Filter listings without a minimum stay of a week or longer
less_than_week = data6[data6['minimum_nights'] < 7]

plt.figure(figsize=(8, 8))
sns.histplot(week_or_longer['price'], bins=50, kde=True, color='blue', label='Week or longer')
sns.histplot(less_than_week['price'], bins=50, kde=True, color='red', label='Less than a week')
plt.title("Istanbul: Distribution of price by minimum stay")
plt.legend()
plt.show()

min_stay_week = data6[data6['minimum_nights'] >= 7]
no_min_stay_week = data6[data6['minimum_nights'] < 7]

avg_price_min_stay_week = min_stay_week['price'].mean()
avg_price_no_min_stay_week = no_min_stay_week['price'].mean()
print(f"\nIstanbul: Average price for listings with minimum stay of a week or longer: ${avg_price_min_stay_week:.2f}")
print(f"Istanbul: Average price for listings without minimum stay of a week or longer: ${avg_price_no_min_stay_week:.2f}")


# **** End for Airbnb Istanbul's Data Set ****