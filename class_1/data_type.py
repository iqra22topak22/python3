# data type in python
# string
# integer (int)
# float
# boolean (bool)
# list
# tuple
# dictionary
# set


#1, string
user_Name:str = "iqra"
print(user_Name)
print(type(user_Name))

#2 integer (int)
your_age = 23
print(type(your_age))
print(your_age)

#3, float
pi_value = 3.142
print(type(pi_value))
print(pi_value)

# 4,boolean (bool)
is_student = True
print(type(is_student))
print(is_student)

# 5 , list
friends_name :list[str]=["sadaf", "dua", "sumiya", "iqra"]
print(friends_name)

list_data :list[int]=[1,2,3,4,5]
print(list_data)

# 6, tuple
fruits = (" apple", " banana", "orange", "kiwi")
print(fruits)
print(fruits[2])

# 7, dictionary
user_data: dict[str,str]= {
    "name" : "iqra",
    "f_name": "mushtaq",
    "age":"23",

}

print(user_data["age"])
user_data["name"]="dua"
print(user_data["name"])

#8, set

my_set = {1, 2, 3, 4, 5}
print(my_set)

# set 
num_set = {1,2,2,3,3,4,5,}
print("set numbers", num_set)