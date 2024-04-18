# ===============================================created by Harshil Chavda==================================================================


# this symbol (#) is use to write comment


# a = 10 #is integer
# a = 10.0 #is float
# a = True #is boolean
# a = False #is boolean
# a = "a" #is cherecter is define char


# input() this is input function




# name = input("enter your name : ")
# sname = input("enter your sarname : ")
# age = (input("enter your age : "))
# print(name + "'" + "s" + " age" + " is" +" "+ age + " years" + " old.")
# print(name + " is a genius.")


# a = int (input("enter your first number : ")) 
# b = int (input("enter your second number : "))
# c = (a+b)
# print ("the sum of two numbers are :" , a+b )



# ---------------------------------------------methods----------------------------------------------------
# name = "harshil chavda"
# print(name.upper())
# print(name.lower())
# print(len(name))
# print(name.capitalize())
# print(name.find(h))
# print(name.count())
# print(name.isupper())
# print(name.replace("chavda", "hacker"))
# print(name.replace("c", "h"))
# print("h" in name)


# -------------------------arithmetic operators-----------------------------
# print(10+12) #ans is sum
# print(10-12) #ans is minus
# print(4/2) #ans is division but this ans is floting
# print(4//2) #ans is division but this ans is only integer
# print(2*2) #ans is multiply
# print(3**3) #ans is 3 power of 3
# print(3%3) #ans is remender




# -------------------------comparison operators-----------------------------
# print(20>30) #ans is in boolean
# print(20>=30) #ans is in boolean
# print(20<30) #ans is in boolean
# print(20<=30) #ans is in boolean
# print(20==30) #ans is in boolean
# print(20!=30) #ans is in boolean and ! is not operator that means not_equal



 
# -------------------------logical operators-----------------------------
# print(20==20 and 20==30) #ans is False and this write to this type print(20==20 & 20==30)
# print(20==20 and 20==20) #ans is true this write to this type print(20==20 & 20==20)
# print(20==20 or 30==20) #ans is true this write to this type print(20==20 | 30==20)
# print(20==20 or 20==20) #ans is true this write to this type print(20==20 | 20==20)
# print(20<20 or 20!=20) #ans is false this write to this type print(20<20 | 20!=20)
# print(20<20 not 20!=20) #ans is true
# print(20==20 not 20==20) #ans is false



# -------------------------identity operators-----------------------------
# a = "python"
# b = "python"
# print(a is not b) #ans is False
# print(a is b) #ans is True




# -------------------------membership operators-----------------------------
# name="hacker"
# print('p' in name ) #True if p present else flase
# print('p' not  in name) #True if p present else flase





# -------------------------continue statement-----------------------------
# for i in range (1,6):
#     if i == 4: 
#         continue   #if condition is true then it will skip the loop
#     print("end")




# -------------------------break statement-----------------------------
# for i in range (1,6):
#     if i == 4:
#         break
#     print ("hello world")




# -------------------------pass statement-----------------------------
# def myfunc(): pass    ##this function do nothing but we can use this keyword to avoid error
# myfunc()



# -------------------------if and else statement-----------------------------
# name = input("enter your name :")
# age = input("enter your age :")
# if (age >= 18): # if this statment is true so this run and false so else ststement run
#     print ("you are eligible for voting ")
# else:
#     print ('sorry you are not eligible to voting')




# -------------------------nested if and else statement-----------------------------
# marks= int(input())
# grade='F'
# if ((marks>=95)):
#    grade ='A+'
# elif((marks>74)&(marks<=94)):#elif mean else if
#   grade ="A"
# elif((marks >64)&(marks <=73)):
#   grade = 'B'
# elif((marks <64)|(marks ==64)):
#   grade = 'C'
# else:
#   grade = 'D'
# print(grade)




# -------------------------def fuction-----------------------------
# def sum():
#      num_one =int(input("Enter first number"))
#      num_two =int(input("Enter second number"))
#      return num_one+num_two
# print(sum()+20)




# -------------------------switch statement-----------------------------

# Implement Python Switch Case Statement using Dictionary

# --------------------------------end switch steatement---------------------------------------






# --------------------------------for loop---------------------------------------
# for i in range(1,10):
#     print('hello world',i,'times')

# ---------------------------for loop example-------------------------------
# this code is make table

# num = int(input("enter the number : "))

# for i  in range (1, 11): 
#     print(str(num) + "X"+str(i) + "=" + str(i*num))





# --------------------------------while loop---------------------------------------
# --------------------------------nested while loop---------------------------------------
# i = 0
# while i < 6:
#   i += 1
#   if i == 3:
#     continue
#   print(i)


# --------------------------------nested while loop---------------------------------------
# i = 1
# while i <= 4 :
#     j = 0
#     while  j <= 3 :
#         print(i*j, end=" ")
#         j += 1
#     print()
#     i += 1



 
# --------------------------------list---------------------------------------
# list = [1,2,3,4,5,6,7,8,9]
# print(list)


# --------------------------------list indexing---------------------------------------
# list[0] ans is 1

# list[-1] ans is last element of a list

# list[:] ans is all elements of that list

# list[:3] ans is first three elements from index zero to nine.

# list[::2] ans is every second element starting with one and ending at ninth position

# list[::-1] ans reverse order of list





# --------------------------------list methods---------------------------------------

# list.append(10) # add element at last of array

# list[len(list)]=10    #add element at last index using len function

# list[-1]=10           #add element at last index using negative indexing

# list.insert(-1,10)    #add element at specific position use insert method and pass two parameter first one is postion second

# del list[0]          #delete first element from array

#del list[:2]            # delete elements between start and stop indexes




# --------------------------------list iterating---------------------------------------
# list = ["hacker", " coder", "gamer", "youtuber"]
# for i in list:
#     print("Hello "+i+"!")



# --------------------------------adding element in list---------------------------------------
# car_name=[]   #create empty list or list name
# car =  int(input("enter number of car in the list : "))
# for x in range (0,int(car)):
#    car_name.append(input("enter the car name : "))
# print("printing the list...")
# for i in car_name:
#    print (i,end="   ")




# --------------------------------removing in list---------------------------------------
# l = [1,2,3,4,5,6]
# print ("Original List:", l)
# l.remove(2)   #remove 2
# print ('After removing:', l)





# --------------------------------tuples---------------------------------------
# t=(1,"hello")      #tuple with two values
# print(t)             #(1,'hello')
# print(type((1)))       #<class 'tuple'>






# --------------------------------tuples operation---------------------------------------
# tup=("a","b","c","d","e")        #creating tuple
# print('tup',len(tup))           #'tup' length is five
# print(tup[-1])                 #'e' last value
# print(tup[::-1])               #[‘e’, ‘d’, ‘c’, ‘b’, ‘a’]
# print(tup*2)                  #[‘a’, ‘b’, ‘c’, ‘d’, ‘e’, ‘
#                                 a’, ‘b’, ‘c’, ‘d’, ‘e’]
# print(tup+('f','g'))          #[‘a’, ‘b’, ‘c’, ‘d’, ‘e
#                                 f’, g’]
# print(tup[:],tup())            #[‘a’, ‘b’, ‘c’, ‘d’, ‘e']
# print(tup==tup)                True
# print(tup!=tup)                False
# print(tup<tup)                 TypeError: '<' not supported between instances of 'str' and 'str'
# print(tup>tup)                 TypeError: '>' not supported between instances of 'str' and 'str'
# print(tup<=tup)                TypeError: '<=' not supported between instances of 'str' and 'str'
# print(tup>=tup)                TypeError: '>=' not supported between instances of 'str' and 'str'
# print(tup is tup)              True
# print(tup is not tup)          False
# print(tup in tup)              TypeError: argument of type 'tuple' is not iterable
# print(tup not in tup)          TypeError: argument of type 'tuple' is not iterable







# --------------------------------tuples example---------------------------------------
# tup=('apple','banana','cherry')     #create tuples
# for x in tup:                       #iterate through the tuple
#    print (x)                        #print each item


# fruits=['mango','guava','pineapple']         #list of fruit names
# for i in range(0,3):                     #looping through list
#   if fruits[i]=='pineapple':             #if pineapple found then break loop
#     break                               #break statement ends execution
# else:                                     #else part will execute when
#   print ('all fruits are good')          #no condition satisfies
# print ("Good bye!")                      #goodbye message






# --------------------------------set and set methods---------------------------------------
# set={'a','b'}                   #{‘a’,'b'}, no duplicates allowed
# print(type({}))                 #<class 'dict'>
# print({'a'})                    #{‘a’}, but duplicate values will be removed
# print(set.add('c'))             {‘a’,'b','c'}
# print(set.update(['d']))        {‘a’,'b','c','d'}
# print(set.remove('a'))          {'b', 'c', 'd'}
# print(set.discard('z'))         {'b', 'c', 'd'}  discard() method ignores non-existent elements without raising
# print(set.discard('z'))         {'b', 'c', 'd'}  discard() method ignores non-existent elements without raising
# print(set.discard('z'))         {'b', 'c', 'd'}  discard() method doesnot raise error even if element





# --------------------------------set examples---------------------------------------
# my_set = {"apple", "banana"}      #creating a new empty set object
# thisset = set(("apple", "banana")) #creating a new set with elements from sequence
# print(my_set)                     #printing original set
# print(thisset)                    #printing new set
# print("ban" in thisset)           #check whether an element belongs to a set or not
# for elem in my_set:               #iterating over set
#     print(elem + "\n")            #prints all items one after another




# --------------------------------set examples with subtrection---------------------------------------
# car_showroom_1 = {"Rolls-Royce Phantom", "Rolls-Royce Phantom Extended", "Rolls-Royce Cullinan", "Rolls-Royce Ghost", "Rolls-Royce Ghost Extended", "Rolls-Royce Black Badge Series", "Rolls-Royce Spectre"}
# car_showroom_2 = {"Rolls-Royce Phantom", "Rolls-Royce Phantom Extended", "Rolls-Royce Cullinan", "Rolls-Royce Ghost", "Rolls-Royce Ghost Extended", "Rolls-Royce Black Badge Series", "Rolls-Royce dawn"}
# car_showroom_3 = {"Rolls-Royce Phantom", "Rolls-Royce Phantom Extended", "Rolls-Royce Cullinan", "Rolls-Royce Ghost", "Rolls-Royce Ghost Extended", "Rolls-Royce dawn"}

# print("this car is not avileble in any 1 car showroom :",car_showroom_1-car_showroom_2)

# ------------------------------------set examples using ^ operator----------------------------------------
# print("this car is available at both the car showrooms:",car_showroom_1^car_showroom_2)

# --------------------------------------set comperison examples----------------------------------------
# c = car_showroom_1<=car_showroom_3
# print (c)
# d = car_showroom_1<=car_showroom_3
# print (d)

# -------------------------------------set type-------------------------------------
# print ("the data type of car_showroom_1 is ",type(car_showroom_1))   #dictionary


# ----------------------------set example--------------------------------------
# student = {"name": "mehul", "age":18, "id":22, "phone no." : 1234567890}
# print("name : %s" %student["name"])
# print("id : %d" %student["id"])
# print("age : %d" %student["age"])
# print("phone no. : %d" %student["phone no."])

# ----------------------------set example delete--------------------------------------
# del student["age"] 


# ----------------------------set pop method--------------------------------------
# x=student.pop('name')    #deleting name key and value pair form dictionary
# print(x)


# ---------------------------built-in dictionary method--------------------------------------
# dict1={"a":"b","c":"d","e":"f"}
# print(dict1.__len__())       #returns length of keys present inside dictionary
# print(dict.clear(dict1))
# print(dict.copy(dict1))
# print(dict.items(dict1))
# print(dict.keys(dict1))
# print(dict.update(dict1))
# print(dict.values(dict1))

# --------------------------------------------listing of modules code--------------------------------------
# help("modules")
# moduls list with example :- file:///C:/Users/DELL/OneDrive/Desktop/python%20all%20moduls.pdf     #this line we be not run

# -------------------------------------------rend modules--------------------------------------
# import random as r     #importing module with alias
# print(r.randint(1,100))
# print(r.randrange(1,10))
# print(r.choice([1,"hello"]))      #randomly chooses one element from list or tuple
# print(r.sample(["apple","banana"],k=2))        #chooses k number elements randomly without repetition
# print(r.shuffle(['a','b']))           #shuffles a sequence in place
# print(r.seed(None))                  #resets seed to current time


# ---------------------------------datetime module-----------------------------------------------
# from datetime import date          #importing only specific class/function from the library
# todaydate=date.today()             #getting today's date using built function
# print("\nToday's Date: "+str(todaydate)+"\n")
# # ---------------------------------------time module--------------------------------------------------
# from datetime import *               #importing all classes/functions from the library
# now=datetime.now().strftime("%H:%M:%S")         #formatting time string
# print("\nCurrent Time is:"+ str(now)+ "\n")


# ---------------------------------datetime example-----------------------------------------------
# import datetime
# datetime.time
# datetime_object = datetime.datetime.now()
# print(datetime_object)
# print("year :", datetime_object.year)
# print("month :", datetime_object.month)
# print("day : ", datetime_object.day )
# print("hour : ", datetime_object.hour)
# print("minute : ", datetime_object.minute)
# print("second : ", datetime_object.second)
# print("timezone infom : ", datetime_object.tzinfo)



# ----------------------------------------------matplotlib modules-----------------------------------------
# step-1 install this module

# link -: https://pypi.org/project/matplotlib/


# # ----------------------------------------------matplotlib example-----------------------------------------
# import matplotlib
# from matplotlib import pyplot as plt
# plt.plot([1,2,3],[4,5,1])
# plt.show()


# example 1
# import matplotlib
# from matplotlib import pyplot as plt
# x=[0, 1 ,2]   #[0,1,2], [6,7,8]
# y=[9, 8, 7 ]    #(0+9), (1+8),(2+7)
# plt.bar(x,[i for i in y if i>5 ])    #if condition check and plot bar graph of greater than 5
# plt.show()
# print('hi')


# example 2
# from matplotlib import pyplot as plt     # importing plotting module
# plt.pie([10,20,30],labels=['apple','banana', 'orange'])      # pie chart with labels
# plt.title('my first piechart')       # title to my pie chart
# plt.legend(['first','second','third'],loc='best')        # legend on top right corner
# plt.axis('equal')           # equal axis
# plt.show()

# example 3
# import numpy as np         # importing numpy library
# from matplotlib import pyplot as plt          # importing plotting module
# plt.scatter(np.random.randint(-10,10,size=10),
#             np.random.randint(-10,10, size=10))            # scatter plot
# plt.xlabel('X label')              # X label name\
# plt.ylabel('Y Label')             # Y label name
# plt.title('Scatter Plot Example')               # Title Name
# plt.grid(True,'major' ,'y')                #'major' is major grid line and 'y' is vertical lines
# plt.show()