import random
letters = ['alphabet']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*']

print("PythonPassword Generator!")
nr_letters = (input("How many letters would you like to choose in your password?\n"))
nr_numbers = (input(f"How many numbers would you like to choose?\n"))
nr_symbols = input(f"How many symbols would you like to choose?\n")

if not nr_letters.isdigit() or not nr_numbers.isdigit() or not nr_symbols.isdigit():
    print("Invalid value, please enter a number instead.")
else:
    password = []

random_letter = random.randint(0,51)
for i in range(0, int(nr_letters)):
    random_letter = random.randint(0,51)
    password.append(letters[random_letter])

random_number = random.randint(0,9)
for i in range(0, int(nr_numbers)):
    random_number = random.randint(0,9)
    password.append(numbers[random_number])

random_symbol = random.randint(0,8)
for i in range(0, int(nr_symbols)):
    random_symbol = random.randint(0,8)
    password.append(symbols[random_symbol])

random.shuffle(password)
print(f"Your password: {''.join(password)}")

if len(password) <= 5:
    print("Your password is too weak, try to include at least 8 characters for a stronger password.")

elif len(password) == 7:
    print("Your password is medium, try to include at least 8 characters for a stronger password.")

else:
    print("Your password is strong.")


    
