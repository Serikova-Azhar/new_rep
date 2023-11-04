import random

def is_prime(x: int) -> bool:
    if x <= 1:
        return False
    if x <= 3:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    i = 5
    while i * i <= x:
        if x % i == 0 or x % (i + 2) == 0:
            return False
        i += 6
    return True


def primes(count: int):
    prime_list = []
    num = 2
    while len(prime_list) < count:
        if is_prime(num):
            prime_list.append(num)
        num += 1
    return prime_list


def checksum(x):
    checksum_value = 0
    for num in x:
        checksum_value = (checksum_value + num) * 113 % 10000007
    return checksum_value

def pipeline():
    random.seed(100)  
    prime_list = primes(1000)  
    random.shuffle(prime_list)  
    result = checksum(prime_list)  
    return result


if __name__ == "__main__":
    result = pipeline()
    print(result)
    




