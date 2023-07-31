# Leetcode problem 1672
#Richest Customer Wealth
#method to find richest customer wealth
def richestCustomerWealth(accounts):
    wealth = 0
    #loop to iterate on 1d lists
    for i in range(len(accounts)):
        #loop to iterate on elements of 1d lists
        for j in range(1,len(accounts[i])):
            #storing wealth at first index of eash list
            accounts[i][0]+=accounts[i][j]
            #comparing the maximum wealth
        if(wealth < accounts[i][0]):
            wealth = accounts[i][0]
    return wealth

accounts = [[1,2,3],[4,5,6]]
print(richestCustomerWealth(accounts))