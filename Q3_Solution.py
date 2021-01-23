num = 600851475143

def is_sosu(num):
        for i in range(2,num):
                if num % i == 0: return False
        return True

while not is_sosu(num):
        for i in range(2, num):
                if num % i == 0:
                        num = num // i
                        break
print(num)