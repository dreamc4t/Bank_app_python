class Account:

    def __init__(self, accNum, accType, balance):
       # account_type = ('debit account', 'credit account', 'savings account')

        self.account_number = int(accNum)
        self.account_type = accType
        self.account_balance = float(balance)
        #self.balance = 1337.23

    # Meny
    ### lägg till account som argument
    def account_menu(self):
        a = -1
        self.print_account_info()

        while a != 0:
            # print(f'Account of {self.owner} ')
            # print(f'{self.account_type} with account number {self.account_number}')
            # print(f'Balance: {self.balance}')
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
                break
            elif a == 2:
                self.deposit()
            elif a == 3:
                self.print_account_info()
            elif a == 4:
                break
            elif a == 5:
                self.transaction_history()

    # change account
    def change_account(self):

        print(f'1. {"account x"}')
        print(f'2. {"account y"}')

        a = input("Choice: ")
        if a == 1:
            self.account_menu()

    # saldo, kontotyp (str), kontonummer (unikt)

    # insättningar, uttag, get kontonummer,
    #### def deposit(pnr, account_id, amount)
    #### Gör en insättning på kontot, returnerar True om det gick bra annars False
    def deposit(self):
        amount = input("How much to deposit?: ")
        self.account_balance += float(amount)
        print(f"New balance: {self.account_balance}")

    # transaction history
    def transaction_history(self):
        print("transaction histoororororory")

    # withdraw function
    #### def withdraw(pnr, account_id, amount)
    #### Gör ett uttag på kontot, returnerar True om det gick bra annars False.
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
                print(f'\nYou withdrew {amount}kr\nYour current balance is now {self.account_balance}kr\nGood bye!')

                return False

    # presentera kontot; visa kontonummer, saldo, kontotyp
    #### def get_account(pnr, account_id)
    #### Returnerar Textuell presentation av kontot med kontonummer som tillhör kunden (kontonummer, saldo, kontotyp).
    def print_account_info(self):
        print(f"Account number: {self.account_number}")
        print(f"Account type: \t{self.account_type}")
        print(f"Balance:\t{self.account_balance} kr")




