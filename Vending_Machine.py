print("Welcome to the UB Vending Machine")
print("Enter the number of nickels you wish to insert: ")
number_of_nickels = input()
in_dollar = float(number_of_nickels)*0.05
rdollar = round(in_dollar,2)
balance=float(rdollar)
print("you inserted" +' ' + str(rdollar) +' ' +"dollars")
total_purchase = 0.0
#balance = 0.0
def main_menu():
    print("-----------------------------------\n"
          "Main menu:\n"
          "-----------------------------------\n"
          "[1] Drinks\n"
          "[2] Snacks\n"
          "[3] Exit\n"
          "Select an option <3 to exit>: ")
def drinks_menu():

    while True:
        print("-----------------------------------\n"
          "Drinks menu:\n"
          "-----------------------------------\n"
          "Water    $0.75\n"
          "Juice    $0.99\n"
          "Soda     $1.39\n"
          "Select a drink by entering the full name <x to exit to the main menu>\n")

        choice = input("Drink option: ")
        choice = str(choice)
        if choice == "Water":
            global balance
            balance = float(balance) - 0.75
            global total_purchase
            if(balance >0):
                print("Vending water, you have", str(balance), "dollars left")
            else:
                print("you don't have enough money to buy Water <", str(rdollar), "<", str(0.75), ">")

        elif choice == "Juice":
            balance = float(balance) - 0.99
            if(balance >0):
                print("Vending Juice, you have", str(balance), "dollars left")
            else:
                print("you don't have enough money to buy Juice <", str(rdollar), "<", str(0.99), ">")
        elif choice == "Soda":
            balance = float(balance) - 1.39
            if(balance >0):
                print("Vending Soda, you have", str(balance), "dollars left")
            else:
                print("you don't have enough money to buy Soda <", str(rdollar), "<", str(1.39), ">")
        elif choice == "x":
            return main_menu()
        else:
            print("invalid option!")

def snacks_menu():

    while True:
        print("-----------------------------------\n"
          "snacks menu:\n"
          "-----------------------------------\n"
          "Chips    $0.99\n"
          "Peanuts  $0.5\n"
          "Gum      $1.35\n"
          "Select a snack by entering the full name <x to exit to the main menu>\n")

        choice = input("Snack option: ")
        choice = str(choice)
        if choice == "Chips":
            global balance
            balance = float(balance) - 0.99
            global total_purchase
            if(balance >0):
                print("Vending water, you have", str(balance), "dollars left")
            else:
                print("you don't have enough money to buy Chips <", str(rdollar), "<", str(0.99), ">")

        elif choice == "Peanuts":
            balance = float(balance) - 0.5
            if(balance >0):
                print("Vending Juice, you have", str(balance), "dollars left")
            else:
                print("you don't have enough money to buy Peanuts <", str(rdollar), "<", str(0.5), ">")
        elif choice == "Gum":
            balance = float(balance) - 0.35
            if(balance >0):
                print("Vending Gum, you have", str(balance), "dollars left")
            else:
                print("you don't have enough money to buy Gum <", str(rdollar), "<", str(0.35), ">")
        elif choice == "x":
            return main_menu()
        else:
            print("invalid option!")

while True:

    main_menu()
    choice = input()
    choice = int(choice)
    if choice == 1:
            drinks_menu()
    elif choice == 2:
            snacks_menu()
    elif choice == 3:
            print("-------------------------------\n"
                  "Inserted amount: ", str(rdollar),",", "total purchase: ", rdollar-balance, ",", "change: ", balance)
            exit()
    else:
            print("invalid option!")
