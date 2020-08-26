def arithmetic_arranger(problems, give_sum=False):
    # Check to see if max 5 problems given
    if len(problems) > 5:
        return "Error: Too many problems."
    top_line = ""
    mid_line = ""
    eq_line = ""
    sum_line = ""
    four_space = "    "
    for arithmetic_problem in problems:
        nums_ops = arithmetic_problem.split()
        error_msg = error_check(nums_ops)
        if(error_msg != ""):
            return error_msg
        max_len = len(max(nums_ops, key=len)) + 2
        top_line += nums_ops[0].rjust(max_len, " ") + four_space
        mid_line += nums_ops[1] + nums_ops[2].rjust(max_len-1, " ")\
            + four_space
        eq_line += "-"*max_len + four_space
        sum_line += sum_func(nums_ops).rjust(max_len, " ") + four_space
    arithmetic_problems = top_line.rstrip() + "\n" + mid_line.rstrip()\
        + "\n" + eq_line.rstrip()
    if give_sum:
        arithmetic_problems += "\n" + sum_line.rstrip()
    return arithmetic_problems


def error_check(nums_ops):
    if len(nums_ops) != 3:
        return "Error: Input is Formatted incorrectly"
    # Check that correct operator used
    elif nums_ops[1] != "+" and nums_ops[1] != "-":
        return "Error: Operator must be '+' or '-'."
    # Check it see if digits are numbers only
    elif not nums_ops[0].isdigit() or not nums_ops[2].isdigit():
        return "Error: Numbers must only contain digits."
    # Check to see if digit length greater than 4
    elif len(nums_ops[0]) > 4 or len(nums_ops[2]) > 4:
        return "Error: Numbers cannot be more than four digits."
    else:
        return ""


def sum_func(nums_ops):
    top_num = int(nums_ops[0])
    bot_num = int(nums_ops[2])
    if nums_ops[1] == "+":
        return str(top_num + bot_num)
    elif nums_ops[1] == "-":
        return str(top_num - bot_num)
    else:
        return "Error in sum_func method"
