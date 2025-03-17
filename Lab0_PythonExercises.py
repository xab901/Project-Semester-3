import random

# Exercise 1: Double the input number
print("\n--- Exercise 1 ---")
number = float(input("Enter a number: "))
print(f"Twice your number is: {number * 2}")

# Exercise 2: Name in uppercase
print("\n--- Exercise 2 ---")
name = input("Enter your name: ")
print(f"Your name in uppercase is: {name.upper()}")

# Exercise 3: Number guessing game
print("\n--- Exercise 3 ---")
random_number = random.randint(10, 20)
while True:
    guess = int(input("Guess the number (between 10 and 20): "))
    if guess == random_number:
        print("Congratulations! You guessed it correctly!")
        break

# Exercise 4: Age-based discounts
print("\n--- Exercise 4 ---")
age = int(input("Enter your age: "))
if age <= 19:
    print("You qualify for student discounts!")
elif age >= 55:
    print("You can receive senior discounts!")
else:
    print("You qualify for no age discounts.")

# Exercise 5: Factorial using while loop
def factorial_while(n):
    result = 1
    while n > 0:
        result *= n
        n -= 1
    return result

print("\n--- Exercise 5 ---")
num = int(input("Enter a number to calculate factorial (while loop): "))
print(f"Factorial of {num} is: {factorial_while(num)}")

# Exercise 6: Factorial using for loop
def factorial_for(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print("\n--- Exercise 6 ---")
num = int(input("Enter a number to calculate factorial (for loop): "))
print(f"Factorial of {num} is: {factorial_for(num)}")

# Exercise 7: Student names with Evans surname
print("\n--- Exercise 7 ---")
studentNames = ["Lisa", "Liam", "Leo", "Larry", "Linda"]

# Print current list with Evans surname
print("Current list:")
for name in studentNames:
    print(f"{name} Evans")

# Add new name to the list
new_name = input("\nEnter a new name to add to the list: ")
studentNames.append(new_name)

# Print updated list with Evans surname
print("\nUpdated list:")
for name in studentNames:
    print(f"{name} Evans")
