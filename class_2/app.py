text :str= "hello world"
number:int = 10
decimal_value: float= 10.5
boolean:bool= True
collection_of_data:list[int]=[1,2,3,4,5,6]  #muatble
print(collection_of_data[-1])     #immutable
immutable_collection_of_dats:tuple[int,str,float]=(1,"sadaf",1.5)
object_data:dict[str,str]={"name":"iqra", "f_name": "m.mushtaq"}
print(object_data["f_name"])
unique_value:set[int]={1,1,12,33,44,5,5,6}  #muatble
print(unique_value)
unique_value:frozenset[int]={1,1,12,33,44,5,5,6} 
print(unique_value)

number_list:list[int]=range(1,20)
print(number_list)
print(type(number_list))


for num in range(1,20):
    # list_of_numer:list[int]=[]
    # list_of_numer.append(num)
    print(num)


print(chr(65))

a=6
b=a
b=7
print(id(a))
print(id(b))
print(id(b))

c = 8
print(c)
print(type(c))
c:str=c
print(type(c))


c :int =8
if  type(c)==int:
    print("c is an intger")

else()


print(isinstance(c,int))
print(isinstance(c,float))