#computing the sum of first 'n' integers
def sum_of_n(n):
    the_sum = 0
    for i in range(1,1+n):
        the_sum =the_sum + i
    return the_sum

print(sum_of_n(1000))              
