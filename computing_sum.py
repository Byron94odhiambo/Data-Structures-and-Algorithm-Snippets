#computing the sum of first 'n' integers
#Formula One
def sum_of_n(n):
    the_sum = 0
    for i in range(1,1+n):
        the_sum =the_sum + i
    return the_sum

print(sum_of_n(1000))              


#Formula Two
def summation_of_n(n):
    return (n*(n+1)/2)


print(summation_of_n(1000))    