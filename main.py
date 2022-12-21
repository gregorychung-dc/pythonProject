# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def get_user_name():
    inp = input("Enter your name: ")
    display_name(inp)


def display_name(value: str):
    print(f"Hello {value}!")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    get_user_name()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
