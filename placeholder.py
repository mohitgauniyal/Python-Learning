variable = "Vishal"
print(variable + " is 5 years old") #with concatenation
sent = "%s is 5 years old" #with a placeholder
print(sent%variable) #printing the string with a variable
print(sent%"Kumar") #printing the string with a value
sent = "%s is %d years old" #with string and int placeholders
print(sent%("vishal",5))#passing the values