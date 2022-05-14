import statistics as std
from turtle import st

friends = [5,5,4,5,6,7,8,3,3,4,5,7,8,2,1,3,5,7,8,1,1,2,6,7,9]

# Population
mean = std.mean(friends)
mode = std.mode(friends)
median = std.median(friends)
pstdev = round(std.pstdev(friends), 2)
pvar = round(std.pvariance(friends), 2)
srange = (max(friends) - min(friends))

print("Descriptive Statistics | Population")
print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", pstdev)
print("Variance:", pvar)
print("Range:", srange)

# Sample Data
import array as arr 

sample_data = arr.array('i', friends)
dataset = sample_data[0:5]
data_list = dataset.tolist()

svar = round(std.variance(data_list), 2)
stdev = round(std.stdev(data_list), 2)

print("\nDescriptive Statistics | Sample Population")
print("Sample Data Standard Deviation: ", stdev)
print("Sample Data Variance:", svar)
