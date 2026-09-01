# print("hello")

# print("hello world!")



# age=int(input("enter your age"))
# if age>=18:
#     print("you are eligible to vote")

# else:
#     print("not eligible")



# age=input("tell me your age")
# print(age)


# x=10
# print(type(x))


# z="Lavanya"
# print(type(z))


# y=True
# print(type(y))



# int()
# x=int("10")
# print(x)
# print(type(x))



# float()
# x=float("20")
# print(x)
# print(type(x))



# str()
# x=str("20")
# print(x)
# print(type(x))



# is_student=True
# is_logged_in=False
# print(type(is_student))


# name="lavanya"
# print("My name is",name)


#range:-----------------------------------------------------------------

# r=range(5)
# print(list(r))



# r=range(1,5)
# print(list(r))


# r=range(1,5,2)
# print(list(r))



# data={10,20,30,30}
# print(data)
# print(type(data))


# student={
#     "name":"lavanya",
#     "age":20,
# }
# print(student["name"])




# a=[1,2,3]
# b=[1,2,3]
# print(a is not b)



#for loop:------------------------------

# list = [1,2,3,4,5]
# for i in range(2):
#   print(i)


# str = "hello"
# for i in range(5):
#     print(i)


#while loop:----------------------------

# ab = 10
# while ab >= 5:
#     print("i am running")
#     #ab = ab-1


# a = 0
# while a < 3:
#     if a == 2:
#         continue
#     print(a)
#     a = a+1



# for i in range(5):
#         for j in range(3):
#             print(i*j, end="")



#Tuple:-------------------------------

#Tuple packing:-

# numbers = (10,20,30,40)
# print(numbers)


#Tuple Unpacking:-

# numbers = (10, 20, 30,40)
# a, b, c ,d = numbers 
# print(a) 
# print(b) 
# print(c) 
# print(d)

#Tuple Methods:------------------------

#count():-

# numbers = (1, 2, 2, 3, 2)
# print(numbers.count(2)) 


#index():-

# numbers = (10, 20, 30, 40) 
# print(numbers.index(30)) 



#Nested if Statement:- 

# age = 10
# citizen = "Africa"

# if citizen == "indian":
#     if age >= 18:
#         print("you can vote")
#     else:
#         print("can't vote")
# else:
#     print("you are not indian")


#dictionary:-----------------------

# shallow copy:-

# import copy 

# d1 = {"a":1, "b":2}
# d2 = d1.copy()
# d2 ["a"] = 10
# print(d2)

# # deep copy:-

# d3 = copy.deepcopy(d1)
# d3["a"] = 100
# print(d2)


#match:---------------------

# day = 3

# match day:
#     case 1:
#         print("Monday")

#     case 2:
#         print("Tuesday")

#     case 3:
#         print("Wednesday")

#     case _:
#         print("Invalid day")


#function:---------------------

# def sum(a):
#     return(a)
# sum(5)
# print()



# list = [1,2,3]
# print(len(list))


#iterator:-----------------------

# nums =[10,20,30]
# it = iter(nums)
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())



# from datetime import datetime
# dt = datetime(2026,6,1,10,30)
# print(dt)


# from datetime import datetime
# dt = datetime.now()
# print(dt.year)
# print(dt.month)


# from datetime import datetime
# date_str = "2026-08-15"
# dt=datetime.strptime(date_str,"%Y-%m-%d")
# print(dt)
# print(type(dt))                      


# from datetime import timedelta,datetime
# today=datetime.now()
# next_week=today+timedelta(minutes=7)
# print(next_week)


# JSON module:------------------
# (loads)

# import json
# data ='{"name":"lavanya","age":19}'
# python_data=json.loads(data)
# print(python_data)
# print(type(python_data))

# (dumps)

# import json
# data={"name":"lavanya","age":"19"}
# json_data=json.dumps(data)
# print(json_data)
# print(type(json_data))


#recursion:---------------------

# def printNumber(n):
#     if n==6:
#         return
#     print(n)
#     printNumber(n+1)
# printNumber(1)


#factorial:----------------------

# def fact(n):
#     if n == 0 or n == 1:
#         return 1
#     return n*fact(n - 1)
# print(fact(5))

#addition:------

# def add(n):
#     if n == 0 or n == 1:
#         return 1
#     return n+add(n - 1)
# print(add(5))



# def sumDigit(n):
#     if n==0:
#         return 0
#     return (n%10)+sumDigit(n//10)
# print(sumDigit(1234))


#decorator:----------------------------------

# def hello():
#     print("hello")
# def decorator(func):
#     def wrapper():
#         print("before function")
#         func()
#         print("after function")
#     return wrapper

# hello1 = decorator(hello)
# hello1()


#@syntax:----------------------------------------

# def decorator(func):
#     def wrapper():
#         print("before function")
#         func()
#         print("after function")
#     return wrapper
# @decorator
# def hello():
#     print("heyyy")
# hello()


#Decorator with Arguments:---------------------------------

# def decorator(func):
#     def wrapper(name):
#         print("Before function")
#         func(name)
#         print("After function")
#     return wrapper
# @decorator
# def greet(name):
#     print("Hello", name)
# greet("Lavanya")


#Using *args and **kwargs:------------------------------

# def decorator(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return result
#     return wrapper
# @decorator
# def add(a, b):
#     return a + b
# print(add(10, 20))


#lambda function:-----------------------------

# nums=[1,2,3,4]
# squares=list(map(lambda x:x**2,nums))
# print(squares)


# nums=[1,2,3,4,5]
# even=list(filter(lambda x:x%2==0,nums))
# print(even)
   

#generator:--------------------------------

# def numbers():
#     yield 1
#     yield 2
#     yield 3
# g = numbers()
# print(next(g))
# print(next(g))
# print(next(g))



# squares = [x*x for x in range(5)]
# print(squares)


# squares = (x*x for x in range(5))
# for i in squares:
#     print(i)


# def infinite_count():
#     n = 1
#     while True:
#         yield n
#         n += 1
# g = infinite_count()
# print(next(g))
# print(next(g))
# print(next(g))









# 1. Create a list using comprehension and print it
# list=[i for i in range(10)]
# print(list)

# 2. names=["John","Alex"] convert this in uppercase n print
# names=["John","Alex"]
# UpperCase=[i.upper() for i in names]
# print(UpperCase)
   
# 3. even numbers
# even_num=[i for i in range(1000) if i%2==0]
# print(even_num)

# 4. list=["qwert","ertyui","xcv","ertyui","sdftyui"] print names w more than 5 length
# list=["qwert","ertyui","xcv","ertyui","sdftyui"]
# result=[i for i in list if len(i)>5]
# print(result)

# 5.
# square_dict={i:i*i for i in range(5)}
# print(square_dict)

# 6.
# words=["python","go","java"]
# result={i:len(i) for i in words}
# print(result)









# student={
#     "name":"lavanya",
#     "age":19
#     }
# new_student=student
# print(new_student)


# student={
#     "name":"lavanya",
#     "age":19
#     }
# new_student=student.copy()
# new_student["name"]="roy"
# print(new_student)


# import copy
# student={
#     "name":"lavanya",
#     "skills":["python","docker"]
#     }
# new_student=student.copy()
# new_student=copy.deepcopy(student)

# new_student["skills"].append("redis")
# print(new_student)


#error handling:----------------------------

# try:
#     num = int(input("Enter a number: "))
#     result = 100 / num
# except ZeroDivisionError:
#     print("Cannot divide by zero.")
# except ValueError:
#     print("Please enter a valid number.")
# else:
#     print("Result:", result)
# finally:
#     print("Program Ended")


#oops:------------------

# class Car:
#     def __init__(self):
#        print("car created")
# car1=Car()


#que1:-create a student class with name,marks as data and method is_pass() that return true if marks is >= 40 else false ?

# class student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
    
#     def is_pass(self):
#         if self.marks>=40:
#             return True
#         else:
#             return False
# student1=student("alex",90)
# print(student1.is_pass())
   

#inheritance:-----------------

# class User:
#     company = "openai"
#     @classmethod
#     def show_company(cls):
#         print(cls.company)
# User.show_company()



# class Employee:
#     def work(self):
#         print("employee working")
# class Developer(Employee):
#     def work(self):
#         print("developer coding")
# dev = Developer()
# dev.work()



# class BankAccount:
#     def __init__(self):
#      self.__balance=100
# obj=BankAccount()
# print(obj.__balance)



# class BankAccount:
#     def __init__(self):
#      self.__balance=100
#     def get_balance(self):
#        return self.__balance
# obj=BankAccount()
# print(obj.get_balance())




# class BankAccount:
#     def __init__(self):
#      self.__balance=1000
#     def deposit(self,amount):
#        self.__balance=amount
#     def withdrow (self,amount):
#        if amount<=self.__balance:
#           self.__balance -=amount
#        else:
#           print("sucess amount")
#     def get_balance (self):
#        return self.__balance
# account=BankAccount()
# account.deposit(500)
# account.withdrow(200)
# print(account.get_balance())





# import asyncio
# async def main():
#     print("prog st")
#     await asyncio.sleep(2)
#     print("down file")
#     await asyncio.sleep(3)
#     print("program finish")
# asyncio.run(main())





# import asyncio 
# async def hello(name):
#     print(f"{name} started")
#     await asyncio.sleep(2)
#     print(f"{name} finished")
# async def main():
#     await asyncio.gather(
#         hello("A"),
#         hello("B")
#     )
# asyncio.run(main())





# import asyncio
# async def hello():
#     print("hello")
#     await asyncio.sleep(2)
#     print("world")
# asyncio.run(hello())







# import asyncio
# async def main():
#     print("program start")
#     await asyncio.sleep(2)
#     print("Down file")
#     await asyncio.sleep(3)
#     print("program finish")
# asyncio.run(main())








# async def hello(name):
#     print (f"{name} started")
#     await asyncio.sleep(2)
#     print(f"{name} finish")
# async def main():
#     await asyncio.gather(
#         hello("A"),
#         hello("B")
#     )
# asyncio.run(main())
    




# async def hellow():
#     print("hello"),
#     await asyncio.sleep(2)
#     print("world")
# asyncio.run(hellow())




import asyncio
# async def hello():
#     return "Hello world"
# result=hello()
# result=asyncio.run(hello())
# print(result)
  
# async def, await, asyncio.run




# async def work():
#     print("start")
#     await asyncio.sleep(2)
#     print("end")
# async def main():
#     await work()
#     print("finish main")
# asyncio.run(main())




# async def work():
#     print("start")
#     await asyncio.sleep(3)
#     print("end")
# async def main():
#     task = asyncio.create_task(work())
#     print("main continue")
#     await task
#     print("finish main")
# asyncio.run(main())




# async def one():
#     await asyncio.sleep(2)
#     return "one"
# async def two():
#     await asyncio.sleep(2)
#     return "two"
# async def main():
#     result = await asyncio.gather(
#         one(),
#         two()
#     )
#     print(result)
# asyncio.run(main())










 
