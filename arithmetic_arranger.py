def arithmetic_arranger(problems, show_answer = False):
# Setting up Variables
    results = []        # list of arithmetical results 
    first_line = ''
    second_line = ''
    third_line = ''
    fourth_line = ''
    n = 0

# Catching Exceptions and Preparing Input
    # If there are too many problems supplied to the function: 
    if len(problems) > 5:
        print("Error: Too many problems.")
        return

    # list of operations further subdivided into terms
    all_terms = [ problem.split(' ') for problem in problems ]

    # list of longest numbers of each operation
    maxs = [ max([len(term[0]), len(term[2])]) for term in all_terms ]

    # Each number (operand) should only contain digits:
    for term in all_terms:
        try:
            op1 = int(term[0])
            op2 = int(term[2])
        except:
            print("Error: Numbers must contain only digits.")
            return

        # Only operations allowed are addition and subtraction:
        if term[1] == '+':
            results.append(op1 + op2)
        elif term[1] == '-':
            results.append(op1 - op2)
        else:
            print("Error: Operator must be either '+' or '-'.")
            return 

    # Each operand has a maximum of four digits:
    for l in maxs:
        if l > 4:
            print("Error: Numbers cannot be more than four digits wide.")
            return

# Arranging Arithmetic Expression
    # Each line:
    for n in range(len(all_terms)):
        first_line += f'{all_terms[n][0]:>{maxs[n] + 2}}    '
        second_line += f'{all_terms[n][1]} {all_terms[n][2]:>{maxs[n]}}    '
        dash = '-' * (maxs[n] + 2)
        third_line += f'{dash:>{maxs[n] + 2}}    '
        fourth_line += f'{results[n]:>{maxs[n] + 2}}    '
# Concatenating lines and optionally showing answer to operations
    if show_answer == True:
        arranged_problems = first_line +'\n'+ second_line + '\n' + third_line + '\n' + fourth_line
    elif show_answer == False:
        arranged_problems = first_line +'\n'+ second_line + '\n' + third_line 

    return arranged_problems
