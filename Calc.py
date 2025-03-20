def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1/n2

operations  = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/": divide


}
def calc():
    y_n = True

    num_1 = int(input("What is you first number? :"))
    while y_n:

        for symbols in operations:
            print(symbols)
        operation_symbol = input("Enter the operation you wish to perform :")
        num_2 = int(input("Enter your second number : "))
        answer = operations[operation_symbol](num_1, num_2)
        print(f"{num_1} {operation_symbol} {num_2} = {answer}")
        choice = input(f"Type in y if you wish to continue the calculation with {answer} or type n to end calculation ")

        if choice == "y":
            num_1 = answer
        else:
            y_n = False
            print("\n" * 20)
            calc()



calc()
