shopping_list = ["Apple","Banana"] #to create items list
print(shopping_list)
print(shopping_list[0:1]) #to print first two items from the list.
shopping_list.append("Mango") #to add items in the current list.
print(shopping_list)
del shopping_list[0] #to delete items from the list.
print(shopping_list)
shopping_list[1] = "MANGO" #to update the list item.
print(shopping_list)
print(len(shopping_list))
list_num = [0,1,2,3,4,44,5] #new list
print(min(list_num)) #to print min.
print(max(list_num)) #to print max.
union_list = shopping_list + list_num #union of lists
print(union_list)
multiply_content = shopping_list * 2 #double the list items
print(multiply_content)
