while True:
    try:
        count_1 =  int(input("Enter first count: "))
        count_2 =  int(input("Enter second count: "))
        count_3 =  int(input("Enter third count: "))
        numbers = {count_1, count_2, count_3}

        question_1 = input("You wanna add other count?(yes/no): ")
        if question_1.lower() == "yes":
            adding_count = int(input("Enter count that you would like add: "))
            numbers.add(adding_count)
            print(numbers)
        elif question_1.lower() == "no":
            print("Sure!")
            print(numbers)
        else:
            print("Invalid value")
            continue   
        
        question_2 = input("Maybe you wanna delate count?(yes/no): ")
        if question_2.lower() == "yes":
            try:
                count_delate = int(input("Enter count with you wanna delate: "))
                if count_delate in numbers:
                    numbers.remove(count_delate)
                    print(numbers)
                else:
                    print("Count is not in set")
            except ValueError:
                print("Invalid value")
                continue
        elif question_2.lower() == "no":
            print("Alright, no numbers removed.")
            print("Final number set: ",numbers)    
            break
        else:
            print("Invalid response. Please type 'yes' or 'no'.")
            continue

        print("Final number set: ",numbers)    
    except ValueError:
        print("Invalid value")
        continue
    break
