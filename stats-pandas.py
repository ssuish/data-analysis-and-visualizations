import pandas as pd

f = [5,5,4,5,6,7,8,3,3,4,5,7,8,2,1,3,5,7,8,1,1,2,6,7,9]

ser = pd.Series(f)
sum_stat = ser.describe(f)

print(sum_stat)