user_input=input("Input a Number= ")
num=int(user_input)
divisor=2
number_prime=True
while divisor < num :
    if (num%divisor)==0 :
        number_prime=False
        break
    else:
        divisor=divisor+1
if number_prime==True :
    print(num,"is Prime Number")
else :
    print(num,"is not Prime Number")
