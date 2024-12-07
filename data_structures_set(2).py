while True:
    try:
        count_1 =  int(input("Enter first count: "))
        count_2 =  int(input("Enter second count: "))
        count_3 =  int(input("Enter third count: "))
        numbers = {count_1, count_2, count_3}

        check_number = input("Would you like to check if a number occurs in a set?(yes/no) ")
        if check_number == "yes":
            count_check = int(input("Enter the number you want to search for in the set: "))
            print(count_check in numbers)                

    except ValueError:
        print("Invalid value")
        continue
    break