#creates the format, in this case we have used 4 emoty{} to insert our strings to
formatter = "{} {} {} {}"
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
# no '' around true and false ad they are recognised by python
print(formatter.format(True, False, False, True))
#prints the fomatter 4 times so 4 lots of {}
print(formatter.format(formatter, formatter, formatter, formatter))
#even thought they are split into different lines, they all print out as one line. better to read this way
print(formatter.format(
    'once upon a time',
    "in a land far far away",
    "there lived a big friendly obi bear",
    "obi was not a bear, he is a cat"
))