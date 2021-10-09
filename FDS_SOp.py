str=input("Enter String : ").lower()
print(" ")

# Longest word in the String.
str1=str.split(" ")
l=0
for i in str1:
  if len(i)>l:
    l=len(i)
    r=i
print("Longest Word in the String is ",r)
print(" ")

# Frequnecy of a particular character in the String. 
x=0
char=input("Enter a char to be serched : ").lower()
for i in range (len(str)):
  if char==str[i]:
    x+=1
print("Frequency of ","char", " is : ",x)
print(" ")

# String is Palindrome or Not.
p=""
for i in str:
  p=i+p
if (str==p):
  print("Palindrome.\n")
else:
  print("Not a Palindrome.\n")

# Word in the String is Palindrome or Not.
str2=str[::-1].split()
str2.reverse()
count=[]
for i in range (len(str1)):
  if (str1[i]==str2[i]):
    count.append(str1[i])
if count!=0:
  print(', '.join(count)," is/are Palindrome word in the String.\n")
else:
  print("String is not a Palindrome.\n")

# Index of first appearance of the Substring.  
sub=input("Enter Substring to be searched : ").lower()
if sub in str1:
  print("Given Substring is present at index ",str.index(sub),"\n")
else:
  print("Given Substring is not present.\n")

# Count the occurrence of each letter  in the String. 
freq={}
for i in str:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print("Frequency of words in the String are \n",freq)


#Output:

#Enter String : Madam wants to meet my Mom and Dad
 
#Longest Word in the String is  madam
 
#Enter a char to be serched : A
#Frequency of  char  is :  5
 
#Not a Palindrome.

#madam, mom, dad  is/are Palindrome word in the String.

#Enter Substring to be searched : Meet
#Given Substring is present at index  15 

#Frequency of words in the String are 
# {'m': 6, 'a': 5, 'd': 4, ' ': 7, 'w': 1, 'n': 2, 't': 3, 's': 1, 'o': 2, 'e': 2, 'y': 1}
