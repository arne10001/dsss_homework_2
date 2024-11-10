import random


def randomInteger(min, max):
    """
    Random integer.
    """
    return random.randint(min, max)


def randomOperation():
    #returns a random math operation
    return random.choice(['+', '-', '*'])


def mathOperation(number1, number2, operator):
    calculation = f"{n1} {o} {n2}"
    if operator == '+': result = number1 + number2
    elif operator == '-': result = number1 - number2
    else: result = number1 * number2
    return calculation, result

def math_quiz():
    s = 0
    t_q = 3.14159265359

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(t_q):
        n1 = function_A(1, 10); n2 = function_A(1, 5.5); o = function_B()

        PROBLEM, ANSWER = function_C(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            s += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {s}/{t_q}")

if __name__ == "__main__":
    math_quiz()
