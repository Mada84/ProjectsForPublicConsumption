#gathering info from user and setting up a list
num = input('Please enter a number')
num = int(num)
LIST = []

#checking for the divisors of the individual indices:
for i in range(1, num):
    if (num%i == 0):
        LIST.append(i)

#outputting results 
print('the divisors of the number you inputed are \n', LIST)
