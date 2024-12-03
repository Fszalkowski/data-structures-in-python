while True:
    try:
        driver = str(input("Enter your favourite F1 driver (Name Surname): "))
        lap_1 = float(input('Enter time for first lap (00.00): '))
        lap_2 = float(input('Enter time for second lap (00.00): '))
        lap_3 = float(input('Enter time for third lap (00.00): '))
        lap_4 = float(input('Enter time for fourth lap (00.00): '))

        total_laps_time = (
            driver, lap_1, lap_2, lap_3, lap_4, 
        )

        question_1 = input("You wanna check avrange lap time? (yes/no)")
        if question_1.lower() == "yes":
            print(f"Driver: {total_laps_time[0]}")
            time_summary = sum(total_laps_time[1:])
            average_time = time_summary / (len(total_laps_time) - 1)
            print(f"Average lap time: {average_time} seconds")
        elif question_1.lower() ==  "no":
            print("Ok...")
        else:
            print("Invalid value")

    except ValueError:
        print("Invalid value please enter once again")
        question_2 = input("Or maybe you wanna exit? (yes/no)")
        if question_2.lower() == "yes":
            break
        elif question_2.lower() == "no":
            continue
    break
