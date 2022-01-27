from Bank import Bank as bank

bank1 = bank("Eriks bank")

try:
    bank1.welcome_menu() #samma som run application
except KeyboardInterrupt:
    print("Error")
finally:
    bank1.update_db()
