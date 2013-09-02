#Given: Positive integers n<=40 and k<=5.

#Return: The total number of rabbit pairs that will be present after n months if
#we begin with 1 pair and in each generation, every pair of reproduction-age
#rabbits produces a litter of k rabbit pairs (instead of only 1 pair).

input_file = 'rosalind_fib.txt'
input = open(input_file, 'r')

numbers = ''.join([line[:-1] for line in input])
[n, k] = [int(num) for num in numbers.split()]

for month in range(n):
    if month == 0:
        rabbits = [1, 0]
    else:
        rabbits = [rabbits[1]*k, rabbits[0]+rabbits[1]]

print sum(rabbits)
