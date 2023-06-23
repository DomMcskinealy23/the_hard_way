name = 'Dom Mcskinealy'
age = 33
height_ft = 5.11
height_inc = height_ft * 12
weight_kg = 75
weight_lbs = weight_kg * 2.205
eyes = 'brown'
teeth = 'yellow'
hair = 'brown'

print(f'lets talks about {name}')
print(f'hes {height_ft} foot tall')
print(f'he is {round(height_inc)} inches tall')
print(f'hes {weight_kg} kilograms')
print(f'his weight in pounds is {weight_lbs}')
print('actually thats not too heavy')
print(f'hes got {eyes} eyes and {hair} hair')
print(f'his teeth are usually {teeth} dependig on the coffee')

#this line is triky, try to get it right
total = age + height_ft + weight_kg
print(f'if i add {age}, {height_ft}, and {weight_kg} i get {total}')
