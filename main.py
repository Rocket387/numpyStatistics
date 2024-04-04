import numpy as np

water_height = np.array([4.01, 4.03, 4.27, 4.29, 4.19,
                         4.15, 4.16, 4.23, 4.29, 4.19,
                         4.00, 4.22, 4.25, 4.19, 4.10,
                         4.14, 4.03, 4.23, 4.08, 14.20,
                         14.03, 11.20, 8.19, 6.18, 4.04,
                         4.08, 4.11, 4.23, 3.99, 4.23])

print(np.mean(water_height)) # average water height, gets to the center of the data set

print(np.sort(water_height)) # sorts the data into order of low to high

print(np.median(water_height)) #used after soring the data set middle value in the data set

print(np.percentile(water_height, 100))#percentile gives the value in a particular percentage

print(np.std(water_height))#standard deviation similarity/variability of data points to the mean
#It represents the typical distance between each data point and the mean. Smaller values indicate
# that the data points cluster closer to the mean—the values in the dataset are relatively consistent.