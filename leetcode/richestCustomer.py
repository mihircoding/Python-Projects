
def maximumWealth(accounts):
    maxWealth = 0
    for i in range(len(accounts)):
        if sum(accounts[i]) > maxWealth:
            maxWealth = sum(accounts[i])
    return maxWealth

sample = [[1,2,3],[3,2,1]]
print(maximumWealth(sample))