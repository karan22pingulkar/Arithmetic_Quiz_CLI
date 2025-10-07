import random
import time

while True:
    display_message = input("Hello, Welcome!!! \n Lets Start  ? ")
    if display_message.lower() == "yes" or display_message.upper() == "YES":
        print("Cool lets start \U0001F37A")
        break
print("This is the main program running...")

for i in range(25):
    a = random.randint(10, 99)
    b = random.randint(10, 99)
    operator = random.choice(['+', '-', '*', '/'])
    if operator == '/':
        # division is always integer
        a = a * b
    if operator == '-':

        if a < b:
            a, b = b, a

    question = f"{a} {operator} {b}"
    start_time = time.time()
    display_numbers = input(f"{question}\n")
    end_time = time.time()
    time_taken = end_time - start_time
    print(f"\U0000231B: {time_taken:.1f} seconds")
    if operator == '+':
        correct_answer = a + b
    elif operator == '-':
        correct_answer = a - b
    elif operator == '*':
        correct_answer = a * b
    elif operator == '/':
        correct_answer = a//b
    else:
        correct_answer = None  # fallback

    try:
        if int(display_numbers) == correct_answer:
            print("Correct Answer \U0001F44D")
        else:
            print(
                f"Wrong Answer \U0001F44E the correct answer is {correct_answer}")
    except ValueError:
        print(
            f"Invalid input. Please enter a number. The correct answer is {correct_answer}")
