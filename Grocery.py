inventory = {"bread":10,"milk":12,"cola":7,"fanta":7,"water":35,"candy":10}

basket = []
total = []

def cashier ():
    user answer = input("Hello there what do you wish to purchase today?").lower()
    while user_answer != "quit":
        if user_answer in inventory:
            basket.append(user_answer)
            user_answer = input("Perfect! i will add that to your basket! anything else you wish to purchase?"
                                "(type 'quit' to end)").lower()
        else:
            user_answer = input("I am truly")
