from stack import Stack


def reverse_string(my_string: str) -> str:
    rev_stack = Stack()

    for i in my_string:
        rev_stack.push(i)

    reversed_str = ''
    while not rev_stack.is_empty():
        reversed_str += rev_stack.pop()

    return reversed_str


if __name__ == "__main__":
    print(reverse_string("hello"))  # olleh
