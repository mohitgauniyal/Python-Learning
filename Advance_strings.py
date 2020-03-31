my_name = "Vishal"
sentence = "This is a sentence."

print(my_name[0:2]) #this prints first two words of my_name
print(my_name[0],my_name[-1]) #this will print first and last word of my_name.
print(sentence.split()) #this will split the sentence in list.
sentence_split = sentence.split()  #stored in variable
sentence_join = ' '.join(sentence_split) #joined the splited sentence
print(sentence_join)

quote = "He said, 'give me all your money'" #we can put single quote in double quote.
quote1 = "He said, \"give me all your money\"" # \" used to use ""
quote2 = "                 hello    "

print(quote)
print(quote1)
print(quote2.strip()) #clear the white spaces
print("A" in "Apple") #check A exists in Apple(Case Sensitive)
letter = "A"
word = "apple"
print(letter.lower() in word.lower())
