import random


def yield_random_integers(min_value, max_value):
    """
    This function will generate the random integer within specified range
    
    Parameters:
    min_value sets the minimimum value for random integer
    max_value sets the maximum value for random integer

    Returns:
    int:Random integer within the specified range
    
    """
    return random.randint(min_value, max_value)


def yield_random_operators():
    '''
    This function generates the random arithmetic operator ('+', '-', '*')

    Returns: 
    str: Random arithmetic operator


    '''
    return random.choice(['+', '-', '*'])


def perform_operation(num_1, num_2, operator):
    '''
    This function performs the arithmetic operation between numbers and operators

    Returns
    tuple: Arithmetic problem as a string and the correct answer

    '''
    problem = f"{num_1} {operator} {num_2}"
    if operator == '+': 
        answer = num_1 + num_2
    elif operator == '-': 
        answer = num_1 - num_2
    else: answer = num_1 * num_2
    return problem, answer

def math_quiz():
    '''
    which will conduct a math quiz game with the user

    '''
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        num_1 =  yield_random_integers(1, 10); 
        num_2 =  yield_random_integers(1, 5); 
        operator = yield_random_operators()

        problem, correct_answer = perform_operation(num_1, num_2, operator)
        print(f"\nQuestion: {problem}")
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print ('invalid input,Please put a valid integer')
            continue

        if user_answer == correct_answer:
            print("Correct! You earned a point.")
            score += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
    
