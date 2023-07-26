import json

def createNewAccount(name, start_balance):
    temp_user = {
        "id": len(accounts["accounts"]) + 1,
        "owner_name": name,
        "balance": start_balance
    }
    accounts["accounts"].append(temp_user)
    with open("rome.json", "w") as file:
        json.dump(accounts, file)



def withdraw_funds(user_id, balance):
    for i in accounts["accounts"]:
        if i["id"] == user_id:
            if i["balance"] - balance >= 0:
                i["balance"] -= balance
                print(i["balance"])
                return
            else:
                print("Ви ввели занадто велику суму, на вашому рахунку менше, введіть правильну суму")
        else:
            print("Такого користувача не знайдено, спробуйте ще раз ")
    print(accounts["accounts"])
    with open("rome.json", "w") as file:
        json.dump(accounts, file)

def top_up_funds(user_id, balance):
    for i in accounts["accounts"]:
        if i["id"] == user_id:
            i["balance"] += balance
            print(i["balance"])
        else:
            print("Такого користувача не знайдено, спробуйте ще раз ")
    print(accounts["accounts"])
    with open("rome.json", "w") as file:
        json.dump(accounts, file)


def transfer_to_another_user(user_id_sender, user_id_receiver, balance):
    temp_user_id_sender_arr = []
    temp_user_id_receiver_arr = []
    for sender in accounts["accounts"]:
        if user_id_sender == (sender["id"]):
            if sender["balance"] - balance >= 0:
                temp_user_id_sender_arr.append(sender["id"])
                sender["balance"] -= balance
        else:
            print("Такого відправника не знайдено")

    for receiver in accounts["accounts"]:
        if user_id_receiver == receiver["id"]:
            temp_user_id_receiver_arr.append(receiver["id"])
            receiver["balance"] += balance
    with open("rome.json", "w") as file:
        json.dump(accounts, file)

    print(f"""{accounts["accounts"][user_id_sender-1]} - sender """)
    print(f"""{accounts["accounts"][user_id_receiver - 1]} - receiver """)

def check_balance(user_id):
    for i in accounts["accounts"]:
        if i["id"] == user_id:
            print(f"""{i['owner_name']},  balance - {i['balance']}""")


if __name__ == "__bank__":
    not_exit = True
    with open("rome.json", "r", encoding="utf-8") as file:
        # ________________________________________
        accounts = json.load(file)
        while not_exit:
            main_menu = input("1 - створити аккаунт, 2 - вивести кошти з рахунку, 3 - поповнити ваш рахунок, 4 - зробити переказ на інший рахунок, 5 - перевірити баланс рахунку, вийти з програми - exit:  ")
            if main_menu == "1":
                name_input = input("Введіть як вас звуть: ")
                balance_input = int(input("Введіть свій початковий баланс: "))
                createNewAccount(name_input, balance_input)
                print(accounts)
            elif main_menu == "2":
                user_id_input = int(input("Введіть привласнений аккаунту id: "))
                minus_balance_input = int(input("Введіть суму котру ви хочете зняти:  "))
                withdraw_funds(user_id_input, minus_balance_input)
            elif main_menu == "3":
                user_id_input = int(input("Введіть привласнений аккаунту id: "))
                plus_balance_input = int(input("Введіть суму котру ви хочете поповнити на ваш рахунок: "))
                top_up_funds(user_id_input, plus_balance_input)
            elif main_menu == "4":
                user_sender_id_input = int(input("Ввведіть ваш id аккаунту щоб  перевести кошти: "))
                user_receiver_id_input = int(input("Ввведіть  id аккаунту на котрий ви хочете перевести кошти: "))
                balance_input = int(input("Введіть яку суму ви хочете перевести: "))
                transfer_to_another_user(user_sender_id_input, user_receiver_id_input, balance_input)
            elif main_menu == "5":
                user_id_balance_input = int(input("Введіть привласнений id свого аккаунту: "))
                check_balance(user_id_balance_input)
            elif main_menu == "exit":
                break