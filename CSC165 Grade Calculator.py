#CSC148 Grade Calculator 

# Things you need to fill in.
# Note all values should be in percentages for example if you got 75.51% you would fill in 75.51
# For marks you don't have yet you can put in a projected value.

problem_set_1 = 100
problem_set_2 = 87.5
problem_set_3 = 96.88
problem_set_4= 1
problem_set_5 = 1

midterm1 = 0.6786
midterm2 = 0.75
final = 0.9



# Under the hood
problem_set_1 = problem_set_1*0.01
problem_set_2 = problem_set_2 *0.06
problem_set_3 = problem_set_3 *0.06
problem_set_4= problem_set_4*0.06
problem_set_5 = problem_set_5*0.06
midterm1 = midterm1 *0.14
midterm2 = midterm2 * 0.14
final = final *0.41


def calculate_csc148_mark():
    total_avg = problem_set_1 + problem_set_2 + problem_set_3 + problem_set_4 + problem_set_5 + midterm1 + midterm2 + final
    print("You're projected mark for CSC148: " + str(round(total_avg*100)) + "%")
    print("This was made by Frank (Haolun Li)")

calculate_csc148_mark()