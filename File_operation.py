my_file=open('text.txt',mode='r')
str=my_file.readlines()
print(str)
str=my_file.readline()
print(str)
my_file.close()