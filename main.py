#Tuples
student_detail = ("Niru", 7, "Second Grade")
print(type(student_detail))

#Packing - assigning values to a tuple
address = (246, "Rosewood Court", "Edison", "New Jersey", "08267")
print(address)

for i in address:
    print(i)

#Unpacking - assign values to multiple variables
houseno, apartment, city, state, pin = address
print("House Number : ", houseno)
print("Apartment : ", apartment)
print("City : ", city)
print("State : ", state)
print("Pin : ", pin)

#Tuples can be created WITHOUT parenthesis
pets = "dog", "cat", "bird", "fish"
print(type(pets))

#Nested tuple
myTuple = ("keys",(3,4,5), [76, 14, 33])
print(myTuple[0])
print(myTuple[0][2])

#Tuple is immutable - cannot change a value once it is created
#myTuple[0][2] = "g"

myTuple[2][2] = 100
print(myTuple)

#Concatenation
my_tuple1 = ("pineapple","mango")
my_tuple2 = ("potato", "bhindi")

result = my_tuple1 + my_tuple2
print(result)

ice_cream = ("mango", "oreo", "chocolate", "butterscotch", "vanilla")
print(len(ice_cream))

flower = ("rose","carnations","tulips","violets")
print(flower * 3)

#Slicing
tuple1 = ("C","O","D","I","N","G")
print(tuple1[0:3])
print(tuple1[:3])
print(tuple1[2:6])
print(tuple1[2:])
print(tuple1[:])
print(tuple1[0:-1])