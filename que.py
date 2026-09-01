#                                                     Python Practice Questions

#que1................................

# name = "lavanya"
# print(name)


#que2.................................

# age = 19
# city = "delhi"
# print(age)
# print(city)


#que3.................................

# name = input("enter your name")
# print(name)


#que4.................................

# num1 = int(input("Enter first number "))
# num2 = int(input("Enter second number "))
# sum = num1 + num2
# print(sum)


#que5.................................

# a = 20
# b = 30
# temp = a
# a = b
# b = temp
# print(a)
# print(b)


#que6.................................

# w = 5
# x = 5.0
# y = "5"
# z = True
# print(type(w))
# print(type(x))
# print(type(y))
# print(type(z))

#.............................................................................................................................................

#                                       Python Practice Questions: Loops, Lists, and Strings

#que1.................................

# for i in range(21):
#  if i % 2 == 0:
#     print(i,"even")
#  else:
#     print(i,"odd")


#que2..................................

# numbers = [12, 45, 7, 23, 89, 34, 56, 11, 90, 5]          # sum = 0
# largest = numbers[0]
# # for num in numbers:
# #    sum = sum + num
# #    print(sum)

# for item in numbers:
#    if item > largest:
#       largest = item

#    else:
#       print("items is shorter than largest number")
# print(largest)








# numbers = [12, 45, 7, 23, 89, 34, 56, 11, 90, 5]
# min = numbers[0]

# for item in numbers:
#     if item < min:
#         min = item

#     else:
#         print("larger")
# print(min)


#que3..................................

# character = "Hello Python"
# vowels = "aeiou"
# count = 0

# for ch in character:
#     if ch in vowels:
#         count += 1

# print(count)


#que4..................................

# names = ["Lavanya", "Rashmi", "Sanil", "Soumya", "Zoya"]

# for ch in names:
#     if len(ch) > 5:
#         print(ch)


#que5..................................

# character = "Python"
# reverse = ""

# for i in character:
#     reverse = i + reverse

# print(reverse)


#.............................................................................................................................................

#                         Python Practice Questions Topics: Lists, Tuples, Strings, Loops, Nested If/Else

#que1..................................

# list = [2,3,4,5,6,7,8,9]
# primeList = []

# for num in list:
#     if num > 1:
#         prime = True

#         for i in range(2, num):
#             if num % i == 0:
#                 prime = False
#                 break
#         if prime:
#             primeList.append(num)

# print(primeList)


#que2..................................

# text = "python"
# maxNum = 0
# maxChar = ""
# for ch in text:
#     count = text.count(ch)

#     if count > maxNum:
#         maxNum = count
#         maxChar = ch
# print(maxChar)


#que4..................................

# name=input("")

# for i in name:
#     print(name.count(i))


#que5..................................

# numbers = [1,2,3,4,4,5,6,2,8]
# unique = []

# for num in numbers:
#     if num not in unique:
#         unique.append(num)
# print(unique)


#que7..................................

# p=input()

# if len(p)>=8:
#     print("Valid")
# else:
#     print("Invalid")


#que8..................................

# a=[1,2,3]
# b=[4,5,6]
# c=[]
# for i in range



#que10..................................





#.............................................................................................................................................

#                                                 Python Beginner Practice Problems

#que1..................................

# for i in range(1,11):
#  print(i)


#que2..................................

# for i in range(1,51):
#     if i%2==0:
#      print(i)


#que3..................................

# n=int(input())
# for i in range(1,11):
#     print(n*i)


#que4..................................

# sum=0
# for i in range(1,101):
#     sum+=i
# print(sum)


#que5..................................

# n=int(input())
# if n%2==0:
#     print("Even")
# else:
#     print("Odd")


#que6..................................

# n=int(input())

# if n>0:
#     print("Positive")
# elif n<0:
#     print("Negative")
# else:
#     print("Zero")


#que7..................................

# a = 2
# b = 10
# c = 4
# if a>b and a>c:
#     print(a)
# elif b>c:
#     print(b)
# else:
#     print(c)


#que8..................................

# a=input()
# rev=""

# for i in a:
#     rev=i+rev

# print(rev)


#que9..................................

# character = "Hello Python"
# vowels = "aeiou"
# count = 0

# for ch in character:
#     if ch in vowels:
#         count += 1

# print(count)


#que10..................................

# a=input()

# if a==a[::-1]:
#     print("Palindrome")
# else:
#     print("Not")


#que11..................................

# for i in range(1,6):
#     print("*"*i)


#que12..................................

# n=5
# fact=1
# for i in range(1,6):
#     fact= fact*i
# print(fact)


#que13..................................

# n=input()
# print(len(n))


#que14..................................

# num = 5
# a = 0
# b = 1
# for i in range(num):
#     print(a)
#     c = a+b
#     a = b
#     b = c

#que15..................................

# list = [2,3,4,5,6,7,8,9]
# primeList = []

# for num in list:
#     if num > 1:
#         prime = True

#         for i in range(2, num):
#             if num % i == 0:
#                 prime = False
#                 break
#         if prime:
#             primeList.append(num)

# print(primeList)


#que16..................................

# a=[1,2,3,4]
# print(sum(a))


#que17..................................

# list = [2,4,9,7,1]
# max = list[0]
# for num in list:
#     if num>max:
#         max=num
# print(max)


#que18..................................

# a="hello"
# for ch in a:
#  print(a.count(ch))


#que19..................................

# a="hello world"
# print(a.replace(" ",""))


#que20..................................

# num=5
# guess=int(input())
# if guess==num:
#     print("Correct")
# else:
#     print("Wrong")


#.............................................................................................................................................

#                                        Python Intermediate Level Questions

#que2.................................

# num = [10, -5, 0, 7, -2, 0, 15, -8]
# positive = 0
# negative = 0
# zeroes = 0
# for num in num:
#     if num > 0:
#         positive += 1
#     elif num < 0:
#         negative += 1
#     else:
#         zeroes += 1
# print("Positive numbers:", positive)
# print("Negative numbers:", negative)
# print("Zeroes:", zeroes)


#que3..................................

# def reverse_string(text):
#     rev = ""
#     for i in text:
#         rev = i + rev
#     return rev
# print(reverse_string("hello"))


#que4.................................

# data = (10, 20, 30, 40, 50)
# for i in range(len(data)):
#     print(i,data[i])


#que5.................................

# a = 10
# b = 5
# op = "*"
# match op:
#     case "+":
#         print(a+b)
#     case "-":
#         print(a-b)
#     case "*":
#         print(a*b)
#     case "/":
#         print(a/b)


#que7..................................

# def factorial(n):
#     fact=1
#     for i in range(1,n+1):
#      fact =fact* i
     
#     return fact
# print(factorial(5))

#que9..................................

# color = input()
# match color:
#     case "red":
#         print("Stop")
#     case "yellow":
#         print("Wait")
#     case "green":
#         print("Go")
#     case _:
#         print("Invalid signal")


#.............................................................................................................................................

#             Python Practice Questions (Easy to Intermediate).....Topics: Functions, Iterators, Modules, and Loops

#que1...................................

# def add_numbers(a,b):
#     return a+b
# sum = add_numbers(10,30)
# print(sum)


#que2...................................

# def greet(name,country="delhi"):
#     print(name,country)
# greet("lavanya","mumbai")


#que3...................................



#que4..................................

# for i in range(1,21):
#     if i%2==0:
#      print(i) 


#que5................................

# for i in range(1,6):
#     print("*"*i)


#que6...............................

# num = 10
# while num >= 1:
#     print(num)
#     num -= 1


#que7...............................

# import math
# print(math.sqrt(144))


#que8...............................

# import calculator
# print(calculator.add(10,20))
# print(calculator.sub(20,15))


#que9...............................

# num = [10, 20, 30, 40, 50]
# iterator = iter(num)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))


#que10..............................






#.............................................................................................................................................

#                                           Python *args and **kwargs - Practice Questions

#que1...............................

# def add_numbers(*args):
#     return sum(args)
# print(add_numbers(10,20,30,40))


#que2...............................

# def find_max(*args):
#     return max(args)
# print(find_max(20,10,5,70))


#que3.................................

# def print_user(**kwargs):
#     print(kwargs)
# print_user(role = "admin",name = "lavanya",age = 19)


#que4.................................

# def greet(name,*args):
#     print(name)
#     print(args)
# greet("lavanya","reading","dancing")


#que5..................................

# data = {
#     "name" : "lavanya",
#     "age" : 19
# }
# def user(name,age):
#     print(name,age)
# user(**data)


#.............................................................................................................................................

#                                           Python Scope Practice Questions

#que1................ Local vs Global

# x=100
# def show():
#  x=50
#  print(x)

# show()
# print(x)


#que2................ Reading a Global Variable

# name="lavanya"
# def greet():
#  print(name)
# greet()


#que3.................global Keyword

# count=10
# def increment():
#     global count
#     count+=5
# increment()
# print(count)


#que4.................. nonlocal Keyword

# def outer():
#     x = 20
#     def inner():
#         nonlocal x
#         x += 10
#     inner()
#     print(x)
# outer()


#que5..................LEGB Rule

# x = "global"
# def outer():
#     x = "outer"
#     def inner():
#         print(x)
#     inner()
# outer()

       
#que6.................Bonus Challenge

# x = 100
# def outer():
#     x = 50
#     def inner():
#         global x
#         x += 10
#     inner()
#     print("outer:", x)
# outer()
# print("global:", x)



#recursion:-------------------------------

#que1.........reverse a string using recursion ?

# def reverse(s,i):
#     if i==-1:
#      return ""
#     return s[i] + reverse(s,i-1)
# print(reverse("python",len("python")-1))
    

#que2.........check palindrome ?

# def ch(z):
#     if len(z)<=1:
#         return True
#     if z[0]!=z[-1]:
#         return False
#     return ch(z[1:-1])
# word="dad"                    
# if ch(word):
#     print("palindrome")
# else:
#     print("not palindrome")


#que3.........count digit ?

# def count(n):
#     if n<10:
#         return 1
#     return 1+ count(n//10)
# num =45707424774
# print(count(num))


#.............................................................................................................................................
#                 Python Exception Handling Practice Questions Topics Covered: try, except, else, finally, raise

#que1.....................

# try:
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))
#     result = num1 / num2
# except ValueError:
#     print("Please enter valid numbers.")
# except ZeroDivisionError:
#     print("Cannot divide by zero.")
# else:
#     print(result)
# finally:
#     print("Program Ended")


#.............................................................................................................................................
#  

#que1......................

# class Dog:
#  def __init__(self, name, age):
#         self.name = name
#         self.age = age
#  def bark(self):
#         print(self.name, "says Woof!")
# d1 = Dog("Buddy", 3)
# d1.bark()

#que2.......................

# class Student:
#     def __init__(self, name, grade):
#         self.name = name
#         self.grade = grade
# s1 = Student("Anna", "A")
# print("Grade:", s1.grade)
# s1.grade = "B"
# print("Updated Grade:", s1.grade)


#que3........................

# class Car:
#     def __init__(self, brand):
#         self.brand = brand
#     def show(self):
#         print("Brand:", self.brand)
# c1 = Car("Ford")
# c1.show()


#que4........................

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     def area(self):
#         return self.width * self.height
# r1 = Rectangle(5, 3)
# print("Area:", r1.area())


#que5........................

# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname
#     def printname(self):
#         print(self.firstname, self.lastname)
# x = Person("John", "Doe")
# x.printname()






# def decorator(func):
#     def wrapper(name):
#         print("start")
#         func(name)
#         print("end")
#     return wrapper

# @decorator
# def greet(name):
#     print("hello",name)
# greet("lavanya")



# def decorator(func):
#     def wrapper(*args,**kwargs):
#         result=func(*args,**kwargs)
#         return result
#     return wrapper

# @decorator
# def add(a,b):
#     return a+b
# print(add(10,20))



