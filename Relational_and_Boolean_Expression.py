#Relational Expressions
greater_than = 7>5 #true
less_than = 5<7 #true
greater_than_equalto = 7>=5 #true
less_than_equalto = 5>=7 #false

#Test 'and' & 'or'
testand1 = 7>5 and 5<7 #true
testand2 = 7>5 and 8<7 #false
testor1 = 7>5 or 5<7 #true
testor2 = 7>5 or 8<7 #true

#Test 'not'
testnot = not True #false

print(greater_than,greater_than_equalto,less_than,less_than_equalto,testand1,testand2,testor1,testor2,testnot)