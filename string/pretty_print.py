import tabulate as tb


def pretty_print_array(numpy_array):
    print(tb.tabulate(numpy_array, tablefmt='orgtbl'))


def pretty_print_text_in_red(text):
    print(f'\033[1;31;49m {text} \033[0m')
