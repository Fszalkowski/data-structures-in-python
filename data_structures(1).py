while True:
    try:
        fruit_1 = input("Enter first fruit: ")
        fruit_2 = input("Enter second fruit: ")
        fruit_3 = input("Enter third fruit: ")
        
        fruits = [fruit_1, fruit_2, fruit_3]
        for fruit in fruits:
            if fruit == "banana":
                print("banana is very sweet")
            elif fruit == "lemon":
                print("lemon is so sour!")
            elif fruit == "cherry":
                print("cherry is not good...")
            else:
                print(f"{fruit} it was delicius")
                
        exit_button = input("You wanna exit?(yes/no)")
        if exit_button == "yes":
            break
        elif exit_button == "no":
            continue
        else:
            print("Invalid value")
            continue
    except ValueError:
        print("Invalid value")
        continue
