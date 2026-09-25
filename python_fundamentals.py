# print("Hello World")

server_name = "app01"
server_count = 5
cpu_usage = 72.5
is_production = True 
print(server_name, server_count,cpu_usage)

server_name = "change_App01"
print(server_name)

#Arithematic Operators
a = 15
b = 4
print("Addition:", a + b)  
print("Subtraction:", a - b) 
print("Multiplication:", a * b)   
print("Division:", a / b) 
print("Floor Division:", a // b)  
print("Modulus:", a % b) 
print("Exponentiation:", a ** b) 

#Relational Operators
a = 13
b = 33
print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)

#Logical Operator
a = True
b = False
print(a and b)
print(a or b)
print(not a)

#Membership Operator
x = 24
y = 20
my_list = [10, 20, 30, 40, 50]

if (x not in my_list):
    print("x is NOT present in given list")
else:
    print("x is present in given list")

if (y in my_list):
    print("y is present in given list")
else:
    print("y is NOT present in given list")

#Identity Operator
a = 10
b = 20
c = a
print(a is not b)
print(a is c)

#Data Types
count = 10
cpu = 72.5
signal = 2 + 3j
print(type(count))
print(type(cpu))
print(type(signal))

#Data Type - String
server = "PROD-APP-01"
print(server[0])
print(server[-1])
print(server.lower())
print(server.replace("PROD", "DEV"))


#Data Type - Lists
servers = ["app01", "app02", "db01"]
print(servers)
servers.append("app03")   #Adds an element at the end of the list.
print(servers)
servers.insert(1,"app022") #Adds an element at the specific index in the list.
print(servers)
servers[0] = "web01" # Updating the server name at zero index
print(servers[-1]) # gives you the value of the last index
servers.remove("app022") #removes the first occurence of the element.
print(servers)
servers.pop(2) #removes the element from the specified index of the list.
print(servers)

#Data Types - Tuples
server_info = ("app01", "prod", 8080)
name, environment, port = server_info
print(name)
print(environment)
print(port)
tup= tuple("Kirti") #Using built-in function
print(tup)
#Accessing the tuple
tup = tuple("google")
print(tup[0])
print(tup[1:4])  
print(tup[:3])
# Tuple unpacking
tup = ("Google", "Cloud", "Platform")
# This line unpack values of Tuple1
a, b, c = tup
print(a)
print(b)
print(c)

#Data Type - Set
a set cannot have duplicate values
s = {"Google", "cloud", "Google"}
print(s)
# values of a set cannot be changed
s[1] = "Hello"
print(s)

#Set Operations
s = {"a", "b", "c"}
s.add("d") #used to insert element but automatically removes the duplicate elements
print(s)
b = {"y", "z"}
u = s.union(b) #combines two sets, returns unique values
print(u)
a = {1, 2, 3,"a", "b"}
i = a.intersection(u) #returns values that are common to both sets
print(i)
c = {2, 3, 4}
d = i.difference(c) #returns values that are in the first set but not in second set
print(d)
cl = {1, 2, 3}
cl.clear() #Clear all elements from the set
print(cl)

#Data Type - Dictionary
server = {
    "name": "app01",
    "environment": "prod",
    "port": 8080
}
print(server)
print(server["name"])
print(server.get("port"))
#Adding and updating the dictionary
d = {"name": "Sam"}
print(d)
d["age"] = 21        # Adding a new key-value pair
d["name"] = "Alex"   # Updating an existing value
print(d)
del d["age"]         # Removes an item using its key
print(d)

#Typecasting Examples.
port_text = "8080"
port = int(port_text)

threshold = "75.5"
threshold_value = float(threshold)

print(port)
print(threshold_value)


#List Comprehension
a = [2, 3, 4, 5]
res = [val ** 2 for val in a]
print(res)
res_condition = [val for val in a if val % 2 == 0]
print(res_condition) #Conditional statements in List Comprehension

b = [i for i in range(10)]
print(b) #Creating a list from a range

c = [(x, y) for x in range(3) for y in range(3)]
print(c) #List from nested loops

#Dictionary Comprehension
sq = {x: x**2 for x in range(1, 6)}
print(sq)
#Creating a dictionary form two lists
keys = ['a','b','c','d','e']
values = [1, 2, 3, 4, 5]  
d = {k:v for (k,v) in zip(keys, values)}  
print (d)
#Dictionary comprehension with conditions
e = {x: x**3 for x in range(10) if x**3 % 4 == 0}
print(e)

#Conditional Statements
age = 25

if age <= 12:
    print("Child.")
elif age <= 19:
    print("Teenager.")
elif age <= 35:
    print("Young adult.")
else:
    print("Adult.")

#Nested if/else
age = 70
is_member = True

if age >= 60:
    if is_member:
        print("30% senior discount!")
    else:
        print("20% senior discount.")
else:
    print("Not eligible for a senior discount.")

#For Loop
n = 4
for i in range(0, n):
    print(i)

#Nested Loop
for i in range(1, 5):
    for j in range(i):
        print(i, end=' ')
    print()

#While Loop
retry = 0
while (retry < 3):
    print(retry+1)
    retry +=1

#Break Statement
# Using For Loop
for i in range(5):
    if i == 3:
        break  # Exit the loop when i is 3
    print(i)
    
# Using While Loop
i = 0
while i < 5:
    if i == 3:
        break  # Exit the loop when i is 3
    print(i)
    i += 1

#Pass Statement
for i in range(5):
    if i == 3:
        pass  # Placeholder for future code
    print(i)

#Continue Statement
for i in range(5):
    if i == 3:
        continue  # Skip the rest of the code for i = 3
    print(i)

#Iterator and Iterable
# list of cities
cities = ["Berlin", "Vienna", "Zurich"]

# initialize the object
iterator_obj = iter(cities)

print(next(iterator_obj))
print(next(iterator_obj))
print(next(iterator_obj))
