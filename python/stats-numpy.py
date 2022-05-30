
import numpy as np
import array as arr 

f = [5,5,4,5,6,7,8,3,3,4,5,7,8,2,1,3,5,7,8,1,1,2,6,7,9]

def display_stat():
    print("Mean:", mean)
    print("Median:", median)
    print("Range:", srange)
    print("Pvariance:", pvariance)
    print("Standard Deviation:", pstdev)
    print("Sample Variance:", var)
    print("Sample Standard deviation", sdev)

mean = np.mean(f)
median = np.median(f)
pvariance = round(np.var(f), 2)
pstdev = round(np.std(f), 2)
srange = np.ptp(f)

sample_data = arr.array('i', f)
dataset = sample_data[0:5]
f_s = dataset.tolist()

var = round(np.var(f_s, ddof=1), 2)
sdev = round(np.std(f_s, ddof=1), 2)

display_stat()