
quote = "Everything is good." #variable
print(quote)
print(quote.upper()) #Uppercase method
print(quote.lower()) #lowercase method
print(quote.title()) #Titlecase method

print(len(quote)) #length

name = "Vishal" #string
age = 24 #int
gpa = 7.1  #float

print("My name is " + name + " & my age is " + str(age) + " years old" + " with " + str(gpa) + " GPA." )

age += 1
print(age)

birthday = 2
age += birthday
print(age)

print('\n')

#defining functions

print("In functions")

#fucnction without Arguments:
def who_am_i():    #Function Defined
    name = "Vishal"  # string
    age = 24  # int
    gpa = 7.1  # float

    print("My name is " + name + " & my age is " + str(age) + " years old" + " with " + str(gpa) + " GPA.")

who_am_i()    #Function Called

#function with Arguments:
def add(num1,num2): #we can add many arguments
    num3 = num1 +num2
    return num3

print(add(2,3))

#Square root Function
def square_root(x):
    return x ** .5   #logic

print(square_root(12))

#new line function
def new_line():
    print("\n")
new_line()
print("END")