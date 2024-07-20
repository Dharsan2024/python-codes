def calc():
    print("CALCULATOR")
    
    while True:
        x = float(input("\nEnter the first number: "))
        y = float(input("Enter the second number: "))
        
        print("\nSelect an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        
        operation = input("Enter the number corresponding to the operation (1/2/3/4): ")
        
        if operation == '1':
            result = x + y
            print("\nResult:", x, "+", y, "=", result)
        elif operation == '2':
            result = x - y
            print("\nResult:", x, "-", y, "=", result)
        elif operation == '3':
            result = x * y
            print("\nResult:", x, "*", y, "=", result)
        elif operation == '4':
            if y != 0:
                result = x / y
                print("\nResult:", x, "/", y, "=", result)
            else:
                print("\nError: Division by zero is not allowed.")
        else:
            print("\nInvalid operation choice.")
            continue
        

        cont = input("\nDo you want to perform another calculation? (yes/no): ").lower()
        if cont != 'yes':
            print("\n calculation completed")
            break

calc()
