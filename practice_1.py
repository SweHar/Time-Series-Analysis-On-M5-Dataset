def check_prime(number):
    for divisor in range(2,int(number**0.5)+1):    # square root of a number + 1
        if number%divisor == 0:
            return False
        #divisor += 1
        return  True
class Primes():
    def __init__(self,max):
        self.max = max
        self.number = 1

    def __iter__(self):
        return self
    def __next__(self):
        self.number+=1
        if self.number >= self.max:
            raise StopIteration
        elif check_prime(self.number):
            return self.number
        else:
            return self.__next__()


prime = Primes(10)
for x in prime:
    print(x)

#same logic using generator

def Primes_gen(max):
    number = 1
    while number < max:
        number+=1
        if check_prime(number):
            yield number

prime_gen = Primes_gen(10)
for x in prime_gen:
    print(x)

