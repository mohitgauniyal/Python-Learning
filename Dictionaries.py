#Dictionaries key/value pairs {}
drinks = {"a": 2,"b":3}
print(drinks)
employees = {"finance": ["bob","job","lob"],"sales": ["rohit","pohit","sohit"]}
print(employees)
employees['marketing'] = ["ram","sham"] #one way to add value.
print(employees)
employees.update({"IT": ["google","yahoo"]}) #second way to add value.
print(employees)
drinks['a'] = 5 #update value.
print(drinks) #prints with variable.
print(drinks.get("a")) #only prints value.