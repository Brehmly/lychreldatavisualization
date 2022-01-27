import pandas as pd
import matplotlib.pyplot as plt
number_of_lychrels = None


def get_num_input():
    print("Please input the number of lychrel numbers you would like to try and find:")
    global number_of_lychrels

    try:
        number_of_lychrels = int(input())
        if number_of_lychrels < 1:
            print("Please enter a positive integer")
            get_num_input()
        else:
            number_of_lychrels = int(number_of_lychrels)
            return number_of_lychrels
    except ValueError:
        print("Please enter a positive integer")
        get_num_input()


num_lychrels = get_num_input()
fun_input = 0
iterations = list()
starting_numbers = list()
lychrel_pairs = {
    "Input": starting_numbers,
    "Number of Iterations": iterations
}
highest_iteration = 0


def findlychrel(num_iter, l_input):
    reverse_input = int(str(l_input)[::-1])
    global highest_iteration
    global fun_input
    if l_input == reverse_input:
        iterations.append(num_iter)
        starting_numbers.append(fun_input)
    else:
        try:
            num_iter = num_iter + 1
            findlychrel(num_iter, l_input+reverse_input)
            if num_iter > highest_iteration:
                highest_iteration = num_iter
        except RecursionError:
            print("You reached the maximum recursion depth of python, number " + str(fun_input) +
                  " has no findable palindrome within 10,000 iterations")


for x in range(number_of_lychrels):
    fun_input = x
    findlychrel(0, x)

df = pd.DataFrame(lychrel_pairs)
df.plot(kind='scatter', x='Input', y='Number of Iterations')
plt.show()
