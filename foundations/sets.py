# 1. Find Common Elements Between Two Sets
print("1. Find Common Elements Between Two Set")
set1={2,3,4,5,6,7}
set2={1,3,5,7,2,9}
common= set1 & set2
print(f"set1: {set1}\nset2: {set2} \nCommon Element Between Tow sets:{common}")


# 2. Find Elements Present in One Set but Not in Another
print("2. Find Elements Present in One Set but Not in Another")
difference = set1 - set2
print(f"set1: {set1}\nset2: {set2} \nElements Present in One Set but Not in Another:{difference}")

# 3. Remove Duplicates From a List Using Sets
print("3. Remove Duplicates From a List Using Sets")
num1=[1,2,3,2,3,5,4,4,5,6,7,6,7]
uniq_num=set(num1)
print(f"List: {num1} \nRemove dubplicates elements from List: {uniq_num}")

# 4. Perform Union, Intersection, and Difference on Two Sets
print("4. Perform Union, Intersection, and Difference on Two Sets")
print(f"Set_1: {set1}. \nSet_2: {set2} \nUnion Of Set_1 and Set_2: {set1 | set2}. \nIntersection Of Set_1 and Set_2: {set1 & set2}. \nDifference Of Set_1 and Set_2: {set1 - set2}.")
