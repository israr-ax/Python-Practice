# 1- Create a tuple and convert it into a list.
print("Q:1- Create a tuple and convert it into a list.")
my_tuple=("Ali","Ahmed","Esrar","John")
print(type(my_tuple))
print(my_tuple)
my_List=list(my_tuple)
print(type(my_List))
print(my_List)

# 2-Count the frequency of an element in a tuple
print("Q:2- Count the frequency of an element in a tuple")

my_tuple2=(1,3,4,3,5,2,1,6,3,1)
num=3
freq=my_tuple2.count(num)
print(f"{my_tuple2} \n{num} appears {freq} times ")

# Find the index of an element in a tuple
print("Q:3- Find the index of an element in a tuple")

print(my_tuple2)
rem_depli=[x for i, x in enumerate(my_tuple2) if x not in my_tuple2[:i]]
element=3
fin_index=rem_depli.index(element)
print(f"Remove Duplicate elements from tuples: {rem_depli} \nIndex of {element} : {fin_index}")

# Check if a tuple is a palindrome.
print("Q:4- Check if a tuple is a palindrome.\n Palindrome means sequence that reads the same forwards and backwards")

def plaindrome(t):
    return t==t[::-1]
cities=('KARACHI', "LAHORE","KARACHI")
print(f"cities:{cities} \n{plaindrome(cities)}")

def is_plaindrome(t):
    left=0
    right=len(t)-1
    while left < right:
        if t[left] != t[right]:
            return False
        left +=1
        right -=1
    return True
T=('A','B','C','B', 'A')
Names=('Ali','Ahmed','Zai')    
print(f"Tuple:{T}:      {is_plaindrome(T)}.\nNames:{Names}:     {is_plaindrome(Names)}")
