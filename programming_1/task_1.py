
def is_perfect(n):
    if n < 1:
        return False

    perfect_sum = 0

    for i in range(1, n):
        if n % i == 0:
            perfect_sum += i

    return perfect_sum == n



try:

 min_value = int(input('Enter  minimum value: '))
 if (min_value < 0):
     min_value = int(input('Enter positive minimum value: '))
 max_value = int(input('Enter maximum value: '))
except ValueError:
 print("please enter a number ")
 min_value = int(input('Enter  minimum value: '))
 if (min_value < 0):
     min_value = int(input('Enter positive minimum value: '))
 max_value = int(input('Enter maximum value: '))


print('Perfect numbers from %d to %d are:' % (min_value, max_value))
for i in range(min_value, max_value + 1):
    if is_perfect(i):
        print(i, end=' ')

