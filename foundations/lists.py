''' Create a list of numbers and find:
sum,max,min '''
#LIST     

def max(l1):
    a=sorted(l1)
    b=a[::-1]
    return b[0]


def min(l1):
    a=sorted(l1)
    return a[0]
    
l=[1,2,3,4,5,7,2,6]
l.append(20)
print(l)
total= sum(l)
print(f"The min value in list is {min(l)}.\nThe max value in List is {max(l)}.\nThe Total sum is {total}")

#REMOVE DUPLICATE NUMBER FROM LIST

rem_dup=[x for i, x in enumerate(l) if x not in l[:i] ]
print(f"Remove Duplicate Number in List:  {rem_dup}")



#REVERSE OF A LIST
a=rem_dup[::-1]
print(f"Resverse of list: {a}")

# Find the second largest number in a list
def second_large(num):
    a=sorted(num)
    reversed_list=a[::-1]
    return reversed_list[1]

l1=[10,20,9,5,55,21,8]

print(f"List: {l1} \nThe second largest number in list is {second_large(l1)}")