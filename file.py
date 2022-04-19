file = open("test1.txt", "r")
file.write("hello world!!")
content = (file.readlines())
for line in content:
   print(line)