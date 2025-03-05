# Unary Operators 
x = 10 
y = -x
print("y=",y)

# Logical NOT (not):
a = True
b = not a
print("b =" , b)

# Bitwise NOT (~): 
a = 10 
b = ~a
print("b =", b)

#              1. Arithmetic Operators
# 1. Arithmetic Operators
# Used for basic mathematical operations.

# +	Addition	
a = 5 
b = 5 
result = a + b 
print(result)
# -	Subtraction	
a = 15 
b = 5 
result = a - b 
print(result)
# *	Multiplication	
a = 5 
b = 5 
result = a *b 
print(result)


# /	Division (float)
a = 5 
b = 5 
result = a / b 
print(result)


# //	Floor Division	5 // 2 = 2 (removes decimal part)
a = 5 
b = 5 
result = a // b 
print(result)
# %	Modulus (remainder)

a = 16 
b = 5 
result = a % b 
print(result)

# **	Exponentiation	
a = 5 
b = 5 
result = a ** b 
print(result)

# 2. Comparison (Relational) Operators 
# Comparison Operators: 

# == : Equal to

a =  5
b = 5
result =a == b
print(result)

# != : Not equal to

a =  5
b = 5
result = a != b
print(result)


# > : Greater than
a =  5
b = 5
result = a > b
print(result)

# < : Less than

a =  5
b = 5
result = a < b
print(result)

# >= : Greater than or equal to

a =  25
b = 15
result = a >= b
print(result)

# <= : Less than or equal to

a =  25
b = 15
result = a <= b
print(result)

# 3. Logical Operators 
# Logical Operators

# and: return ture if both statement are true

a = 10 
b = 20 
print(a==10 and a<b and b==20)

# or: return true if one of the statemwnt is true

a= 25
b= 25
print(a==25 or a>b or b==30)

# not: return true if the statement is false
a=10
b=20
print(not a==10)


# 4. Assignment Operators 

# Used to assign values to variables.

# +=	
a = 5
a += 3
print(a)

# -=
a = 8
a -= 5
print(a)

# *=	
a = 8
a *= 5
print(a)

# /=	
a = 8
a /= 5
print(a)

# //=
a = 8
a //= 5
print(a)

# 5. Identity Operators

a = 5
b = 10
c = a
print( a is b)  #false
print( a is not b)  #true
print( a is c)  #true
print( b is c)  #false

# 6. Membership Operators

my_list: list = [1, 2, 3, 4, 5]

print("my_list           = ", my_list)            # [1, 2, 3, 4, 5]
print("3 in my_list      = ", 3 in my_list)       # True
print("10 not in my_list = ", 10 not in my_list)  #true

my_name ="iqra"
print("a" in my_name)
print("w" not in my_name)
print("a" not in my_name)