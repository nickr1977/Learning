name = "Nick Rodriquez"
age = 44 # not a lie
height = 75 # inches
weight = 200 # lbs
eyes = 'Brown'
teeth = 'White'
hair = 'Brown'

height = (height * 2.54)
weight = round(weight * 2.2)

print(f"Let's talk about {name}.")
print(f"I am {height} centimeters tall.")
print(f"I weigh {weight} kilos.")
print("Actually that's not too heavy")
print(f"I have {eyes} eyes and {hair} hair.")
print(f"My teeth are usually {teeth} depending on the coffee.")

# This line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight}, I get {total}. ")

