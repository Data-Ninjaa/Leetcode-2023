# Leetcode Problem 1342
# Numbers of steps to reduce a number 0
# method
def numberOfSteps(num):
    # steps 
    steps = 0
    # until num equals 0
    while(num!=0):
        # checks
        if( num % 2 == 0):
            num = num / 2
        else:
            num = num -1
        #increase steps
        steps = steps+1
    return steps 
print(numberOfSteps(123))


