num = int(input("Enter any number:"))
if num > 1:
    for i in range(2, num):
        if(num % i) == 0:
            print(num, "is not a prime number, it is composite number")
            break
        else:
            print(num,"is a prime number")
elif num == 0 or 1:
    print(num,"is neither prime nor composite")
else:
    print()
