# 1- Create a tuple and convert it into a list.
print("Create a tuple and convert it into a list.")
my_tuple=("Ali","Ahmed","Esrar","John")
print(type(my_tuple))
print(my_tuple)
my_List=list(my_tuple)
print(type(my_List))
print(my_List)

# 2-Count the frequency of an element in a tuple
print("Count the frequency of an element in a tuple")

my_tuple2=(1,3,4,3,5,2,1,6,3,1)
num=3
freq=my_tuple2.count(num)
print(f"{my_tuple2} \n{num} appears {freq} times ")