##Temp Converter Farenheit to Celcius
user_input=input("What is the Temperature?  ")
temp=float(user_input)
celcius=(temp-32)/1.8
print("Temp in celcius=",celcius)
if temp<32 :
    print("It is Freezing")
elif temp>=32 and temp <50 :
    print("Chilly")
elif temp>=50 and temp <90 :
    print("OK")
else :
    print("Hot")
