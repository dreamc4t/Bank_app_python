from Customer import Customer as cus
from Account import Account as acc


class Bank:

    def __init__(self, name):
        self.name = name
        self._load()

    #dictionary som ska innehålla kunderna + konton
    customers_accounts_dict = {}

    #en räknare av hur många kunder banken har
    customer_count = len(customers_accounts_dict)

    # ladda in kunderna samt deras konton via textfil
    def _load(self):
        ## om man skulle vilja skapa ny txt för varje ny bank
        # raw_data_list = open(f"{self.name}_mock_bank_data.txt").readlines()

        raw_data_list = open(f"mock_bank_data.txt").readlines()

        #läsa in filen och föra in i customers_accounts_dict
        for rows in raw_data_list:
            a = rows.replace('#', ':').replace('\n', '').split(':')
            self.customer_count += 1

            cust = cus(a[0], a[1], a[2])
            if len(a) > 3:

                acco = acc(a[3], a[4], a[5])
                if len(a) <= 6:
                    self.customers_accounts_dict[a[0]] = [cust, acco]
                elif len(a) < 10:
                    self.customers_accounts_dict[a[0]] = [cust, acco, acc(a[6], a[7], a[8])]
                elif len(a) > 10:
                    self.customers_accounts_dict[a[0]] = [cust, acco, acc(a[6], a[7], a[8]), acc(a[9], a[10], a[11])]
            else:

                self.customers_accounts_dict[a[0]] = [cust]

    #Uppdaterar textfilen utifrån customers_accounts_dict
    def update_db(self):
        ## om man skulle vilja skapa ny txt för varje ny bank
        ##text_file = open(f"{str(self.name)}_mock_bank_data.txt", 'w')

        text_file = open(f"mock_bank_data.txt", 'w')
        for k, v in self.customers_accounts_dict.items():
            text_file.write(f"{str(v[0]._id)}:{str(v[0].name)}:{str(v[0].pnr)}")
            if len(v) > 1:
                text_file.write(':')
                for x in range(1, len(v)):
                    text_file.write(f"{str(v[x].account_number)}:{str(v[x].account_type)}:{str(v[x].account_balance)}")
                    if x < len(v)-1:
                        text_file.write("#")

            text_file.write('\n')
        text_file.close()

    def close_account(self, account_number):
        for k, v in self.customers_accounts_dict.items():
            for x in range(1, len(v)):
                if account_number == v[x].account_number:
                    print(f"Account {v[x].account_number} removed and {v[x].account_balance}kr returned to {v[0].name}")
                    v[x].remove_transaction_list()
                    del(v[x])
                    return

        print(f"Error! No account number with {account_number} exists")

    def get_customers_accounts_dict(self):
        return self.customers_accounts_dict

    def welcome_menu(self):
        a = -1
        print(f'--- Welcome to {self.name} ---')
        print(f"With a customer count of {self.customer_count} ")
        print("")
        while a != 0:
            print("--- Main menu ---")
            print("-----------------")
            print(f"1. Existing customer")
            print(f"2. New customer")
            print(f"3. Print list of all customers")
            print(f"4. Print list of all customers and their accounts")
            print(f"9. Remove a customer by personal number")
            print(f"0. Exit")
            a = int(input("Choice: "))
            if a == 1:  # logga in eller öppna konto

                ###För att underlätta inlogg i testversionen
                if len(self.customers_accounts_dict) > 0:
                    print('\nHär är några exempel ur databasen för att underlätta: ')
                    a = []
                    count = 0
                    while count != 5 and count < self.customer_count:
                        for _id, customers_accounts_dict in self.customers_accounts_dict.items():
                            a.append([customers_accounts_dict[0].pnr])
                            count += 1
                            if count == 5:
                                break
                            if count == self.customer_count:
                                break
                    print(a)
                    print("")
                ###/

                    flag = True
                    while flag:
                        flag1 = False
                        pnr = input('Enter personal number to log in: ')
                        for k, v in self.customers_accounts_dict.items():
                            if int(pnr) == v[0].pnr:
                                print(f'Welcome {v[0].name} ')
                                # kör nästa interface där konton/kontot hanteras
                                self.bank_menu(int(pnr))
                                flag1 = True
                                flag = False
                                break
                        if flag1 == False:
                            print("No such personal number exists in database")
                            a = input("Try again? y/n: ")
                            if a == 'y' or a == 'Y':
                                continue
                            else:
                                flag = False
                else:
                    print("There are no customers in this bank yet!")

            elif a == 2: #skapa ny kund
                name = input("Your full name: ")
                while True:
                    try:
                        pnr = int(input("Your personal number: "))
                        break
                    except ValueError:
                        print("Only integers allowed!")
                        continue

                while self.add_customer(name, int(pnr)) == False:
                    a = input("Try again? y/n ")
                    if a == 'y' or a == 'Y':
                        name = input("Your full name: ")
                        while True:
                            try:
                                pnr = int(input("Your personal number: "))
                                break
                            except ValueError:
                                print("Only integers allowed!")
                                continue
                    else:
                        self.welcome_menu() #tillbaks till välkomst-miljön

                # se om nya kunden vill öppna account
                a = input("Would you like to open an account as well? y/n: ")
                if a == 'y' or a == 'Y':
                    self.add_account(int(pnr))
                    self.bank_menu(int(pnr))
                else:
                    print("Ok, please return when you want to open an account!\n \n")
                    a = -1

            elif a == 3: #lista på kunderna
                self.print_all_customers()

            elif a == 4: #stor lista med kunder + deras konton
                print(self.print_list_all())

            elif a == 9: #ta bort kund utifrån input
                pnr = int(input("Which personal number of the customer to remove?: "))
                self.remove_customer(pnr)

    def bank_menu(self, pnr): #menyn när du är inloggad

        for a, b in self.customers_accounts_dict.items():
            if b[0].pnr == pnr:
                if len(b) == 1:
                    c = input("You havn't opened any accounts yet, would you like to open one? y/n: ")
                    if c == 'y' or c == 'Y':
                        self.add_account(pnr)


        #Skriver ut options för den inloggade kunden
        print("\nOptions: ")
        temp = ''
        temp_list = []
        for k, v in self.customers_accounts_dict.items():
            if v[0].pnr == pnr:

                while True: #Beroende på hur många accounts kunden har
                    if len(v) == 2:
                        temp = '1. Account 1\n'
                    elif len(v) == 3:
                        temp = '1. Account 1\n2.Account 2'
                    elif len(v) == 4:
                        temp = '1. Account 1\n2. Account 2\n3. Account 3\n'
                    for acc_no in range(1, len(v)):
                        print(f"{acc_no}. Manage {v[acc_no].account_type} {v[acc_no].account_number} (Balance: {v[acc_no].account_balance} kr)")
                        temp_list += str(acc_no)


                    a = input(f"7. Change/update your name\n8. Close an account\n9. Open a new account (3 max)\n0. Log out\nChoice: ")
                    if a == str(0): #logga ut
                        print("Good bye")
                        return False

                    elif a == str(9): #lägga till nytt account
                        self.add_account(pnr)

                    elif a == str(7): #byta kundens namn
                        self.change_customer_name(pnr)

                    elif a == str(8): #stänga ett konto
                        print("\nAccounts:")
                        for acc_no in range(1, len(v)):
                            print(f"{acc_no}. {v[acc_no].account_type} -  Balance: {v[acc_no].account_balance}")
                        b = input(f"Which account to close? (0 to exit): ")

                        for z in temp_list:
                            if b == z:
                                self.close_account(v[acc_no].account_number)
                                break

                    else: #välja konto utifrån input på en siffra i lista (enklare än att skriva acc number tex)
                        for x in temp_list:
                            if a == x:
                                v[int(a)].account_menu()
                                break

    def print_list_all(self): #Stor lista med bankens kunder + accounts
        for k, v in self.get_customers_accounts_dict().items():
            print(f"\nCustomer: {v[0].name}")
            print(f"------")
            for i in range(1, len(v)):
                v[i].print_account_info()
                print("------")
            if len(v) == 1:
                print("No accounts")
                print("------")

    def get_customer(self, pnr): #Oanvänd, men kan implementeras vid behov, printar info om specifik kund
        for k, v in self.customers_accounts_dict.items():
            if pnr == v[0].pnr:
                print(f"- Account info for customer with ID {v[0]._id} -")
                print(f"Name: {v[0].name}")
                print(f"Personal number: {v[0].pnr}")
                if len(v) > 2:
                    print("Accounts:")
                    print("--------")
                else:
                    print("Account:")
                    print("--------")
                for x in range (1, len(v)):
                    v[x].print_account_info()
                    print("--------")

    def add_account(self, pnr): #lägger till account till kunden

        flag = False
        for k, v in self.customers_accounts_dict.items():
            if int(v[0].pnr) == pnr:
                flag = True
                if len(v) >= 4: #testar om kunden redan har bankens maxantal av konton - 3
                    print(f"You already have 3 accounts which is {self.name}'s current maximum per customer")
                    print("Close an account if you want to create a new. ")

                else: #lägger till unikt account_number i ordningen from 1000 och framåt
                    #borttagna kontos kontonummer är up for grabs när de är borttagna
                    set_of_accNum = set()
                    # loopar genom alla account_numbers:
                    for a, b in self.customers_accounts_dict.items():
                        for i in range(1, len(b)):
                            set_of_accNum.add(b[i].account_number)
                    new_acc_num = 1000
                    while new_acc_num in set_of_accNum:
                        new_acc_num += 1

                    print(f"\nCongrats on you new debit account! It has account number {new_acc_num}")
                    first_depo = input("How much would you like to deposit?: ")
                    v.append(acc(new_acc_num, 'debit account', first_depo))

        if flag == False:
            print(f"Customer with personal number {pnr} doesn't exist in database")

    def add_customer(self, name, pnr): #lägger till ny kund

        for k, v in self.customers_accounts_dict.items(): #kollar om personnummer redan finns i databasen
            if pnr == int(v[0].pnr):
                print(f"There already is a customer with this personal number registered: {v[0].name}")
                return False

        print(f"Welcome to {self.name}, {name}!")

        #kolla om banken har 0 kunden, isf sätt igång räkningen på 111111, annars ta nästa på tur
        if len(self.customers_accounts_dict) < 1:
            next_id = 111111
        else:
            next_id = int(k) + 1
        customer_to_add = cus(next_id, name, pnr)

        # om det mot förmodan skulle lyckas bli error
        for k, v in self.customers_accounts_dict.items():
            if next_id == int(v[0]._id):
                print("Error! The ID we tried to impletement already exists. Contact app designer")

        self.customers_accounts_dict[next_id] = [customer_to_add]

        return True

    def remove_customer(self, pnr): #tar bort kund
        while True:
            for k, v in self.customers_accounts_dict.items():
                if int(v[0].pnr) == pnr:
                    temp = self.customers_accounts_dict[k]
                    self.customers_accounts_dict.pop(k)
                    print(f"Customer {k} ({v[0].name}) is removed. ")
                    if len(v) > 1: #om kunden hade accounts - de tas bort här
                        print("Accounts removed:")
                    else:
                        print("- No accounts removed, customer did not have any accounts -")

                    for i in range(1, len(v)):
                        print(f"Account {v[i].account_number} removed and {v[i].account_balance}kr returned to {v[0].name}")
                    return temp
                    break
            print("No customer with that ID exsists in database")
            pnr = int(input("Try again (0 to exit): "))
            if pnr == 0:
                return False
            else:
                continue
        return False

    def change_customer_name(self, pnr): #byter kundens namn
        for k, v in self.customers_accounts_dict.items():
            if int(v[0].pnr) == pnr:
                print(f"Current name is {v[0].name}")
                new_name = input("What would you like to change it to?: ")
                v[0].name = new_name
                print(f"Congrats, your name is now {v[0].name}! \n")
                return True
            else:
                print(f"No customer with personal number {pnr} exists")
                return False

    def get_account(self, account_id): #oanvänd funktion som printar specifik konto-info
        # loopar genom alla account_numbers:
        for k, v in self.customers_accounts_dict.items():
            for i in range(1, len(v)):
                if v[i].account_number == account_id:
                    print(f"Customer: {v[0].name}")
                    v[i].print_account_info()

    def print_all_customers(self): #lista på alla customers i banken
        for k, v in self.customers_accounts_dict.items():
            id = f"Customer-id: {v[0]._id}"
            name = f"Name: {v[0].name}"
            pnr = f"Personal number: {v[0].pnr}"
            print(f"%-22s %-28s %s" % (id, pnr, name))

    # def update_transaction_db(self):
    #     text_file = open("transactions_list.txt", 'w')
    #     text_file.write('')
    #     for k, v in self.customers_accounts_dict.items():
    #         for a in range(1, len(v)):
    #             print(v[a].transaction_history_list)
    #             text_file = open("transactions_list.txt", 'a')
    #             text_file.writelines(v[a].transaction_history_list)
    #             text_file.write('\n')
    #     text_file.close()






