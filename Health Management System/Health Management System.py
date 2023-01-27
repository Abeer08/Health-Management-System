def getDate():
    import datetime
    return datetime.datetime.now()
try:
    name = input('Enter your name: ').capitalize()
    print("Enter what to do?")
    print("1 to log")
    print("2 to retrieve")
    lock_ret = input(">>>")

    if '1' in lock_ret:
        print("\nWhat to log?")
        print("1 for exercise")
        print("2 for diet")
        exer_diet1 = input(">>>")

        if '1' in exer_diet1:
            exercise = input("\nEnter exercise you have done: ")
            name_e1 = name+' exercise'
            with open(name_e1, 'a') as name_a:
                name_a.write("["+str(getDate())+"] "+" - "+exercise+"\n")
                print('Succesfully stored exercise!')

        else:
            diet = input("\nEnter food you have eaten: ")
            name_d1 = name+' diet'
            with open(name_d1, 'a') as name_b:
                name_b.write("["+str(getDate())+"] "+" - "+diet+"\n")
                print('Successfully stored food item!')

    else:
        print("\nWhat to retrieve?")
        print("1 for exercise")
        print("2 for diet")
        exer_diet2 = input(">>>")

        if '1' in exer_diet2:
            name_e2 = name+' exercise'
            with open(name_e2) as ne2:
                print(ne2.read())

        else:
            name_d2 = name+' diet'
            with open(name_d2) as nd2:
                print(nd2.read())
except:
    print("Unexpected Error, Try Again")
