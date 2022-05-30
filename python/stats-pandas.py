import pandas as pd

f = [5,5,4,5,6,7,8,3,3,4,5,7,8,2,1,3,5,7,8,1,1,2,6,7,9]

ser = pd.Series(f)
sum_stat = ser.describe(f)

print(sum_stat)

# Population
pstdev = ser.std(ddof=0)
print(pstdev)

# import and read csv
# df = pd.read_csv("sample.csv")

# display first 10 rows csv
# frows = df.head(10)

# display last 10 rows csv
# lrows = df.tails(10)

# row selection with conditions
# sel = df[df["Country"] == "TW"]

# filter countries using isin()
# sea = df[df["Country"].isin(["Country 1", "Country 2", "Country 3"])]

# summary of stats
# stats = sea["Population (2020)"].describe()

# ranking
# sort_sea = sea.sort_values(by="population(2020)", ascending=false)
