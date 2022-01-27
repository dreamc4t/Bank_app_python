from datetime import datetime

time_right_now = datetime.now() # time object
current_time = time_right_now.strftime("%Y-%m-%d %H-%M")



class Account:

    def __init__(self, accNum, accType, balance):
       # account_type = ('debit account', 'credit account', 'savings account')

        self.account_number = int(accNum)
        self.account_type = accType
        self.account_balance = float(balance)
        self.transaction_history_list = []
        self.load_transactions_from_txt()

    def update_transaction_db(self, transaction):
        text_file = open("transactions_list.txt", 'a')
        text_file.write(transaction)
        text_file.write('\n')
        text_file.close()

    def load_transactions_from_txt(self):
        raw_data_list = open("transactions_list.txt").readlines()
        slask_list = []
        for rows in raw_data_list:
            a = rows.replace('\n', '').split('%')
            if len(a) > 1:
                if int(a[0]) == self.account_number:
                    slask_list.append(a)
        if len(slask_list) > 0: #om det finns transaktioner loggade
            self.transaction_history_list = slask_list

    def remove_transaction_list(self):
        txt = open("transactions_list.txt", "r+")
        raw_data_list = txt.readlines()
        txt.seek(0)
        txt.truncate()

        for row in raw_data_list:
            acc_num_key = int(row[0:4])
            if acc_num_key != self.account_number:
                txt.write(str(row))
            elif acc_num_key == self.account_number:
                txt.write('')

        txt.close()
        self.load_transactions_from_txt()


    def add_to_trans_hist(self, transaction):
        line = str(f"{self.account_number}%{current_time}%{transaction}%{self.account_balance}")
        self.transaction_history_list.append(line)
        self.update_transaction_db(line)
        self.load_transactions_from_txt()



    # Meny
    def account_menu(self):
        a = -1
        self.print_account_info()

        while a != 0:
            print('')
            print('1. Withdraw')
            print('2. Deposit')
            print('3. Print account info')
            print('4. Change account')
            print('5. Transaction history')
            print('0. Exit to main menu')
            a = int(input('Choice: '))

            if a == 1:
                self.withdraw()
            elif a == 2:
                self.deposit()
            elif a == 3:
                self.print_account_info()
            elif a == 4:
                break
            elif a == 5:
                self.print_transaction_history()

    # transaction history
    def print_transaction_history(self):
        if len(self.transaction_history_list) > 0:
            for rows in self.transaction_history_list:
                if float(rows[2]) > 0:
                    operator = '+'
                else:
                    operator = ''
                line = f"Date: {rows[1]} Transaction: {operator}{rows[2]} Balance:{rows[3]}"
                print(line)
            if len(self.transaction_history_list ) > 10:
                input("Press Enter to go back to account menu")

        else:
            print("No transactions has been made with this account yet")

    # withdraw function
    def deposit(self):
        amount = input("How much to deposit?: ")
        try:
            if float(amount) > 0:
                self.account_balance += float(amount)
                print(f"New balance: {self.account_balance}")
                self.add_to_trans_hist(float(amount))

            else:
                print("Error, you must enter a positive amount")
        except ValueError:
            print("Error, only enter numbers and decimal points")

    def withdraw(self):

        while True:
            amount = float(input("How much would you like to withdraw?: "))
            if amount > self.account_balance:
                print(f"{amount}kr is more than you have in your account: {self.account_balance}kr")
                a = input("Would you like to withdraw a lesser amount? y/n: ")
                if a == 'y' or a == 'Y':
                    continue

                else:
                    print('Good bye!')
                    return False
            else:
                self.account_balance -= amount
                print(f'\nYou withdrew {amount}kr\nYour current balance is now {self.account_balance}kr')
                self.add_to_trans_hist(0 - amount)

                return False

    # presentera kontot; visa kontonummer, saldo, kontotyp
    def print_account_info(self):
        print(f"Account number: {self.account_number}")
        print(f"Account type: \t{self.account_type}")
        print(f"Balance:\t{self.account_balance} kr")




