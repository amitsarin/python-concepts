import random
print(" This prog will ask user 8 names of people and store them in list. pick random one and print it")
people_list=[]
while len(people_list)<8:
    name=input("enter the name  of the person: ")
    people_list.append(name)
number=random.randint(0,8)
print(" Entire list is: ", people_list)
print(" random name is: ", people_list[number])

      
