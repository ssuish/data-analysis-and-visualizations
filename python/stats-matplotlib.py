import matplotlib.pyplot as plt
import statistics as stat

f = [5,5,4,5,6,7,8,3,3,4,5,7,8,2,1,3,5,7,8,1,1,2,6,7,9]

# histogram
fig = plt.figure(figsize = (16, 9))
plt.hist(f, bins=8, edgecolor = "black")
plt.xlabel('hours')
plt.ylabel('frequency')
plt.title('Random Variables', fontsize = 14)
plt.plot([stat.mean(f), stat.mean(f)], [0, 9], linestyle="--", color="r")
plt.plot([stat.median(f), stat.median(f)], [0, 10], linestyle="--", color="y")
plt.plot([stat.pstdev(f), stat.pstdev(f)], [0, 9], linestyle="--", color="g")
plt.plot([stat.mode(f), stat.mode(f)], [0, 9], linestyle="--", color="m")
plt.plot([stat.variance(f), stat.variance(f)], [0, 9], linestyle="--", color="c")
plt.text(8,8, 'mean', color="r")
plt.text(8,7.5, 'median', color="y")
plt.text(8,8, 'mode', color="m")
plt.text(8,6.5, 'stdev', color="g")
plt.text(8,6, 'variance', color="c")
plt.show()
