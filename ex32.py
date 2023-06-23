the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#this forst kind of for-loop goes through a list
for number in the_count:
    print(f"This is the count {number}")

#same as above
for i in fruits:
    print(f"a fruit of type: {i}")

#also we can go through mixed lists
#we have to use {} since we dont know whats in it
for i in change:
    print(f"i got {i}")

#we can also build lists, first start with an emoty one
elements = []



#then use the range function to do 0 - 5 counts
for i in range(0, 6):
    print(f"adding {i} to the list")
    #append is a function that lists understand
    elements.append(i)

#now we can print them out too
for i in elements:
    print(f"Element was: {i}")
