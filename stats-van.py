
n_num=[78, 80, 79, 80, 87, 85]
n = len(n_num)

# mean | vanilla
def get_mean (ave):
    print ("Then mean of the list is", ave)
get_sum = sum(n_num)
mean = get_sum / n
m = str(mean)
get_mean(m)

# median | vanilla
import array as arr

def median(nums):
    nums.sort()
    if len(nums) % 2 == 0:
        return int(nums[len(nums) // 2 - 1] + nums [len(nums) // 2]) / 2
    else:
        return nums[len(nums) // 2]

print("Median: ", median(n_num))

# Variance | vanilla
friends = [5,5,4,5,6,7,8,3,3,4,5,7,8,2,1,3,5,7,8,1,1,2,6,7,9]

def print_friends(friends):
    for usage in friends:
        print(usage)
def friends_sum(friends):
    total = 0
    for usage in friends:
        total += usage
    return total
def friends_ave(friends):
    sum = friends_sum(friends)
    ave = sum / float(len(friends))
    return ave
def friend_variance(scores):
    ave = friends_ave(scores)
    variance = 0
    for score in scores:
        variance = variance + (ave - score) ** 2
    return variance/len(scores)
v = round(friend_variance(friends), 2)
print("Variance: ", v)

# Standard deviation | vanilla
def friend_std_dev(variance):
    return variance ** 0.5

variance = friend_variance(friends)
s = round(friend_std_dev(variance), 2)
print("Standard deviation: ", s)