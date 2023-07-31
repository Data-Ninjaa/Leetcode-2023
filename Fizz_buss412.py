#Leetcode problem 412
# Fizz BUZZ
#method
def fizzBuzz(n):
    #list of size n
    answer = [1]*n
    # loop to iterate on list
    for i in range(1,n+1):
        #checks
        if ( i % 3 == 0 ):
            answer[i-1]= "Fizz"
            if( i % 5 == 0):
                answer[i-1] ="FizzBuzz"
        elif(i % 5 == 0):
            answer[i-1] = "Buzz"
        else:
            answer[i-1] = str(i)
    return answer
print(fizzBuzz(5))

