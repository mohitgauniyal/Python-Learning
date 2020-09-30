my_name = "Vishal"
sentence = "This is a sentence."

print(my_name[0:2]) #this prints first two words of my_name
print(my_name[0],my_name[-1]) #this will print first and last word of my_name.
print(sentence.split()) #this will split the sentence in list.
sentence_split = sentence.split()  #stored in variable
sentence_join = ' '.join(sentence_split) #joined the splited sentence
print(sentence_join)
print(sentence[::-1]) #this will reverse the sentence
print(my_name[::-1] == my_name) #this will check if my_name is a pallindrome

quote = "He said, 'give me all your money'" #we can put single quote in double quote.
quote1 = "He said, \"give me all your money\"" # \" used to use ""
quote2 = "                 hello    "

print(quote)
print(quote1)
print(quote2.strip()) #clear the white spaces
print("A" in "Apple") #check A exists in Apple(Case Sensitive)
letter = "A"
word = "apple"
print(letter.lower() in word.lower()) #checks whether it is case sensitive or not.

movie = "The Hangover"
print("My favourite movie is {} but not good." .format(movie)) #print using placeholder
print("My favourite movie is" ,movie) #print only at last.
