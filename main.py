from Bank import Bank as bank

bank1 = bank("Nordea")

try:
    print(bank1.name)
    bank1.welcome_menu()

except KeyboardInterrupt:
    print("Error")
finally:
    bank1.update_db()
