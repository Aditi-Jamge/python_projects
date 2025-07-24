import random
import time

max_problems = 10
signs = ["+","-","*"]

def generate_problems():
    left_digit = random.randint(1,10)
    right_digit = random.randint(1,10)
    operators = random.choice(signs)

    exp = f"{left_digit} {operators} {right_digit}"
    ans = eval(exp)
    return exp, ans

correct = 0

start = input("Press enter to start the challenge!")
print("-----------------------------------\n")

start_time = time.time()
for i in range(max_problems):
    exp, ans = generate_problems()
    while True:
        user = input(f"problem #{i+1} is {exp} = ")
        try:
            if float(user) == ans:
                correct += 1
                break
            else:
                print("wrong!")
                break
        except ValueError:
            print("Invalid Input! Please enter a number.")

end_time = time.time()
final_time = end_time - start_time
print("------------------------------------\n")
print(f"You Correctly answered of {correct} problems.")
print(f"Congrats! You finished in {final_time:.2f} seconds!")

            

        