import numpy as np

patrons = np.array([ 2, 6, 14, 4, 3, 9, 1, 11, 4, 2, 8])

thirtieth_percentile = np.percentile(patrons, 30)
seventieth_percentile = np.percentile(patrons, 70)
print(thirtieth_percentile)
print(seventieth_percentile)

#The 25th percentile is called the first quartile
# The 50th percentile is called the median
# The 75th percentile is called the third quartile

movies_watched = np.array([2, 3, 8, 0, 2, 4, 3, 1, 1, 0, 5, 1, 1, 7, 2])
first_quarter = np.percentile(movies_watched, 25)
third_quarter = np.percentile(movies_watched, 75)

print(first_quarter)
print(third_quarter)

interquartile_range = third_quarter - first_quarter
print(interquartile_range)