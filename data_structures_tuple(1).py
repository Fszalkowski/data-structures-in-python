while True:
    try:
        count_1 = int(input("Enter first value: "))
        count_2 = int(input("Enter second value: "))
        count_3 = int(input("Enter fthird value: "))
        t = (count_1, count_2, count_3)
        
        question_1 = input("With index you wanna show?(1/2/3/all)")
        if question_1 == "1":
            print(t[0]) 
        elif question_1 == "2":
            print(t[1])
        elif question_1 == "3":
            question_1(t[2])
        elif question_1 == "all":
            question_1(t[-1])
        else:
            print("Invalid value")   

    except ValueError:
        print("Invalid value")
        continue

    break