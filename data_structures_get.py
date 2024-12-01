def get_fruit_description(fruit):
    fruit_description = {
        "banana":"banana is very sweet",
        "strawberry":"strawberry is very sweet",
        "mango":"mango is very sweet",
        "apple":"apple is very sweet",
        "blueberry":"blueberry is very sour",
        "lemon":"lemon is very sour",
    }
    return fruit_description.get(fruit, f"{fruit} is so good!")        
while True:
    try:
        fruit_1 = input("Enter first fruit: ")
        fruit_2 = input("Enter second fruit: ")
        fruit_3 = input("Enter third fruit: ")
        
        fruits = [fruit_1, fruit_2, fruit_3]
        for fruit in fruits:
            print(get_fruit_description(fruit))
            
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
