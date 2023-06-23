from sys import argv

script, user_name = argv
prompt = '> '

print(f" Hi {user_name}, im the {script} script. ")
print("id like to ask you a few questions")
print(f"Do you like me {user_name}")
likes = input(prompt)

print(f"where do you live {user_name}")
lives = input(prompt)

print("What ind of computer do you own? ")
computer = input(prompt)

print(f'''
Alright, so you said {likes} about liking me.
you live in {lives}. not sure whwere that is.
And you have {computer} computer. NIce.
''')