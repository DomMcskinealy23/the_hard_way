from sys import argv

script, filename = argv

print(f"We are going to erase {filename}.")
print("if you dont want that, hit CTRL-C (^C).")
print("if you do want that, hit RETURN")

input("?")

print("openeing the file...")
target = open(filename, 'w')

print("Truncating the file.  Goodbye!!")
target.truncate()

print("Now im going to ask you for three lines")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("im going to write to these files")

lines = (line1, line2, line3)
target.write('\n'.join(lines))
target.write('\n')


print("And finally, we close it")
target.close
