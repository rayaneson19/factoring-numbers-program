#factoring program

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** .5) + 1):
        if n % i == 0:
            return False
    return True
print("""      This is a factoring program that gives you the factor of the number you put in.
      
      => you can quit by typing '0'.


""")

v =True

while v:
    num = int(input('                       Type your number:    '))
    if num !=0:
        print(num)
    prime = 0
    i = 2
    while prime < 1000:
        
        if num ==0:
            print('   \n   Thank you for using our programme.   \n   ')
            v = False
            break
        if num % i ==0:
            print(num//i)
        if is_prime(i):
            prime += 1
        i += 1
