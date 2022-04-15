from pickle import TRUE


a = [1,2,3,4,5]
b=[1,21]
#   print(b in a)

for i in b:
    if i in a:
        check = True
    else:
        check = False
        break
if (check == True):
    print("b is subset of a")
else:
    print("b is not subset of a")
 



a = set([1,2,3,4,5])
b = set([1, 22])


print(b.issubset(a))
a = [1, 2, 3, 4 ,5 , 8, 6]
a = ["apple" , "ball" ,"cat" , "aa" ,"bb"]
a.sort(reverse = True)
# a.sort
a = sorted(a)
print(a)