
"""

#s = int(input())
#print(s+1)
print("hello world")


#WEEK 1
#First program is to print 5 numbers

print(1)
print(2)
print(3)
print(4)
print(5)

#Second question is to print a pattern using only print
#Third question is to print sq of a number

x = int(input())
x = x**2
print(x)

#Fourth Question is to print sum of two integers
#Fifth question is to accept two words and print them with space

a = input()
b = input()
print(a+" "+b)

#Sixth question is to Accept a car registration number and print is state code as output

regno = input()
state_code = regno[0: 2]
print(state_code)

#Seventh question is to accept a five digit number as input and print sum of its digits as output

# if five digit not mentioned loop will be used.

num = input()

d1 = int(num[0])
d2 = int(num[1])
d3 = int(num[2])
d4 = int(num[3])
d5 = int(num[4])

dsum = d1 + d2 + d3 + d4 + d5
print(dsum)




#WEEK 2(if,else,elif and import introduced)

#Question 1 is to print if number is positive or negative 
#Question 2 is to take a input as float and print it in form of a f(x) given to you.

#x=float(input())
x = 1
y = x*2
print(y)

#Question 3 is to print something on basis of if,else.
#Question 4 is to print the quadrant of x,y pair given using elif
#Question 5 is to find equation of line using the given points.

#Question 6 is a substring problem, slicing used.

x = input()
y = len(x)

if y%2 == 0:
  print(y)
else:
  y = y-1
  print(y)

print(x[0:y])


#Question 7 to 10 are type of advanced substring quesions

#if word1 in word used.
x = input()
y = len(x)

x1 = x[0:y-1]

if x1 in x:
  print('true')

#Question 8,x.index() function and abs fn introduced

#Question 9 teaches that or & and can be used in if statements.

#Question 10 is about ceil and floor function


#WEEK 3

y=[]
#for x in range(10):
#for x in y:


#In question 1 we print first n numbers
#In question 2 we print the factors of given number n-n%i used
#In question 3 we nothing new 
#Q4 check if a number is prime or not(loop run till given num n and all the number are divided to see no match)

#Q5 (
  Taking input inside a loop uses append method
  For getting last element x[-1] can be used
  break and elif are also be used.
)


print("Type the number of elements")
num = int(input())

for x in range(num):

    y.append(int(input()))
  
    if y[-1] == 0:
      break;

x = 0

for i in y:
  if x>i :
    continue
  elif x<i:
    x = i

print(x)

#Q6 - Print the smallest string given in the input
#Question 7 - Print the sum of integers of the given numbers

x = input()
sum = 0

for i in range(len(x)): 
  sum = sum + int(x[i])

print(sum)
  
n = int(input())
total = 0
while(n > 0):
    total = total + n % 10
    n = n // 10
print(total)


#Question 8 - Print numbers seperated by commas

#Sep and join are introduced here and can be studied for dealing with commas and other things

n = int(input())
for i in range(n):
  print(i , end = ",")

print(",".join([str(i) for i in range(5)]))
print(" cruel ".join(["hello", "world"]))


print("hello", "world", sep=" cruel ")

print(["hello", "world"], sep=" cruel ")#this doesn't give expected result * is used for list
print(*["hello", "world"], sep=" cruel ")
print(*range(5), sep="---")


#Question 9 - Print triangle pattern

x = int(input())

for i in range(x):
  print("0"*i)



#Question 10 - Print sum of all prime numbers till input n              though output is correct, this solution is not optimized

Input = int(input())

prime = True
sum = 0

for current_num in range(2,Input):
  prime = True

  for i in range(2,current_num):
    if current_num%i == 0:
      prime = False
  
  if prime == True:
  #  print(current_num)
    sum = sum + current_num


print(sum)


#Question 11 - 3 for loop can also be used is shown for beginners.

 #if x ** 2 + y ** 2 == z ** 2: print(f'{x},{y},{z}')



#WEEK 4(Lists)

#Question 1 - accept a posicive integer n and print list of first n integers as output

number = int(input())
y = []

for i in range(number):
  y.append(i)

print(y)


#Q2 - Same thing with string

x = int(input())
y=[]

while x!=0:
  y.append(input())
  x = x-1

print(y)


#Q3 - Accept a comma seperated value 

y = input().split(',')

print(y)


#Q4 - A list L of words is already given to you as a part of the prefix code. Print the longest word in the list. If there are multiple words with the same maximum length, print the one which appears at the rightmost end of the list.

L = input().split(',')
max_word, max_len = '', 0 #new format of writing
for word in L:
    if len(word) >= max_len:
        max_len = len(word)
        max_word = word
print(max_word)


#Q5 - Convert each element of the sequence into the greatest integer less than or equal to it.

L = input().split(' ')

for i in range(len(L)):
    L[i] = float(L[i])
    L[i] = int(L[i])
  
for i in range(len(L)):
    if i != len(L) - 1:
        print(L[i], end = ',')
    else:
        print(L[i])


#Q6 - Reverse the sequence and print it as output

x = input().split(',')
y = []

for i in range(len(x)):
  y.append(x[len(x)-i-1])

print(y)


#M2
L = input().split(',')
out = [ ]

for i in range(len(L)):
    out = [L[i]] + out
  
for i in range(len(out)):
    if i != len(out) - 1:
        print(out[i], end = ',')
    else:
        print(out[i])

#Output of both the above methods is different

#Q7 - Accept a square matrix as input and store it in a variable named matrix. The first line of input will be, n, the number of rows in the matrix. Each of the next n lines will have a sequence of n space-separated integers.

#As it is a matrix 2 for loops will be used.

n = int(input())

matrix = [ ]
for i in range(n):
    L = [ ]
    for num in input().split(' '):
        L.append(int(num))
    matrix.append(L)
  
print(matrix)


#Q8,9 and 10 are matrix questions that is why not donw
#Q11 - Introduces you to idea of invisible code and given and unchangable prefix and suffix code

Sorting Question 

sorted_L = [ ]
    while L != [ ]:
        max_elem = L[0]
        for elem in L:
            if elem > max_elem:
                max_elem = elem
        L.remove(max_elem)
        sorted_L.append(max_elem)


#WEEK 5

#Q1 - Write a recursive function for finding factorial of a number

# A break statement and a calling statement is required in a recursive function.

# A factorial even a for loop can be run, infact a for loop can be implemented for any recursive function.

def Facfunc(x):

  if x == 1:
    return x
  else:
    return x * Facfunc(x-1)

y = Facfunc(5)
print(y)


#Q2 - Check if a year is leap year or not

#Should not be a multiple of 100 but of 4 or should be a multiple of both 100 and 400 ie just by 400

def isALeapYear(year):

  if year%4 == 0 and year%100 !=0:
    return True

  elif year%400 == 0:
    return True

  else:
    return False

output = isALeapYear(1956)
print(output)


#Q3 - Accepting 3 integers and printing the maximum value 

#simple if can be used or max func can be used
#print(max(2, 3, 23))
#list1 = [1, 2, 4, 5, 54]
#print(max(list1))


#Q4 - Return true if the dimensions of the given two matrics is same

def dim_equal(A, B):
    return (len(A) == len(B)) and (len(A[0]) == len(B[0]))

#See how rows and columns of matrics are fetched.



#Q5 - Return the first three greatest integers from provided list. You can return multiple values in python return.

#M1 - by sorting
list = [5,4,3,2,1]

def highestthree(list):

  #applying any sorting algorithm here

  return list[0],list[1],list[2]

a,b,c = highestthree(list)
print(a,b,c)

#M2 - 3 pointers and updating
def first_three(L):
    fmax, smax, tmax = L[0], L[1], L[2]

    for x in L:
        if x > fmax:
            tmax = smax
            smax = fmax
            fmax = x
        elif x > smax and x < fmax:
            tmax = smax
            smax = x
        elif x > tmax and x < smax:
            tmax = x

    return fmax, smax, tmax


#Q6 - A simple list length counting question containing strings but you have to see if a certain criteria is satisfied by passing each string to a given function.

def type_of_sequence(words):
    count = 0
    for word in words:
        if mysterious(word):
            count += 1

    if count < 2:
        return 'mildly mysterious'
    elif 2 <= count < 5:
        return 'moderately mysterious'
    else:
        return 'most mysterious'




#Q7 - .Revision of list fetching and concepts of slicing

def is_empty(L):
    return L == [ ]

def first(L):
    if is_empty(L):
        return None
    return L[0]

def last(L):
    if is_empty(L):
        return None
    return L[-1]

def init(L):
    if is_empty(L):
        return None
    return L[:-1]

def rest(L):
    if is_empty(L):
        return None
    return L[1: ]




#Q8 - Implementation of fibonnaci series using recursion

# the thing I tried
count = 0
fibo_num = 1 

def fibo(n,fibo_num,count):

  if count == n:
    return fibo_num

  else:
   count = count + 1
   fibo_num = fibo_num + (fibo_num - 1)
   return fibo(n,fibo_num,count)

x = fibo(3,1,1)
print(x)


#Solution: 
def fibo(n):
    if n == 1 or n == 2:
        return 1
    return fibo(n - 1) + fibo(n - 2)

x = fibo(3)
print(x)





#WEEK 6 - Dictionary and Tuples

x = input().split(',')

for i in x:
  
"""

a = [1,24,35,245,353]

#for i in a:
print(a[:3])
