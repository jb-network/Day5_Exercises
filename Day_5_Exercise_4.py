# # Course Total Python: Become an Advance Python Developer
# Day 5 Exercise 4
def count_primes(passed_number):
    prime_numbers = [2]
    Loop = 3

    if passed_number < 2:
        return 0

    while Loop <= passed_number:
        for num in range(3, Loop, 2):
            if Loop %num == 0:
                Loop +=2
                break
        else:
            prime_numbers.append(Loop)
            Loop += 2
    print(prime_numbers)
    return len(prime_numbers)

#Sample Input
#print(count_primes(50))
#Sample Output
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
# 15
