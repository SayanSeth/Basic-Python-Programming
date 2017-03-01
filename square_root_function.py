#calculates and return the square root of the number
def square_root(input_number):
    square_root=input_number/2
    accuracy=0.0001
    while abs(input_number -(square_root**2))>accuracy:
        square_root=(square_root+(input_number /square_root))/2
    return square_root
#this the main programme
for x in range (1,21):
    y=square_root(x)
    print("Sqaure root of",x,"is",y)