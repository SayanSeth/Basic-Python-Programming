user_input=input("Input a Number to Limit= ")
num=int(user_input)
for x in range(3,num+1):
    divisor=2
    number_prime=True
    while divisor < x :
        if (x%divisor)==0 :
            number_prime=False
            break
        else:
            divisor=divisor+1
    if number_prime==True :
        print(x,"is Prime Number")
    else :
        print(x,"is not Prime Number")
