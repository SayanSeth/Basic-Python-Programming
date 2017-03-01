person={'name':'Sayan','age':20,'weight':60}
print(person)
print(person['age'])
person['job']='student'
print(person)
del person['weight']
print(person)
person['age']=21
print(person)
x=person.get('age')
print("age=",x)
y=person.keys()
print(y)
z=person.pop('name')
print(z)
#dict.clear()
person.clear()
print(person)