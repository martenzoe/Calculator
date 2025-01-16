def calculate(text_input):
    if text_input[1] == "+":
        return int(text_input[0])+int(text_input[-1])
calculation = input("What do you want to calculate?")
answer = calculate(calculation)
print(f"The result is {answer}")