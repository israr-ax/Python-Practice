# 1.Create a Dictionary of Students With Marks and Print Students Scoring Above 80
print("1.Create a Dictionary of Students With Marks and Print Students Scoring Above 80")
students ={
    'ALi':55,
    'Dheeraj':89,
    'Aman':88,
    'pawan':80,
    'israr':79
}
for name , marks in students.items():
    if marks>80:
        print(name, marks)
        
# 2 Count Frequency of Characters in a String Using Dictionary
print("2 Count Frequency of Characters in a String Using Dictionary")
text="Hakari never use reversed cursed technique but negative energy flowing in his body to force him to use reversed cursed technique."
freq={}
for char in text:
    if char in freq:
        freq[char]+=1
    else:
        freq[char]=1
print(f"String: {text} \n{freq}")

# 3.Merge Two Dictionaries Without Using Built-in Merge Methods
print("3. Merge Two Dictionaries Without Using Built-in Merge Methods")
dict1={'a':1,'b':2}
dict2={'c':3,'d':4}

merged={}

for key in dict1:
    merged[key]=dict1[key]
for key in dict2:
    merged[key]=dict2[key]
print(f"Dict_1:{dict1} \nDict_2:{dict2} \nAfter merging both dicts:{merged}")
    