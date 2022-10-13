from math import sqrt

"""List of prime numbers generator."""

def primes(number_of_primes):
    list = []

    counter = number_of_primes
    temp = 0

    while (counter == 0):
        check = False
        if (temp>1):
            #check from 2 to the square root of temp - prime in only those circumstances
            for i in range(2, int(sqrt(temp))+1):
                if (temp % i != 0):
                    check = True
            #if temp is prime, add it to list
            if (check == True):
                list.append(temp)

        temp = temp +1
        counter = counter -1

    return list
