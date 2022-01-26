from Bank import Bank as bank
from DataSource import DataSource as ds



fw = open('tester.txt', 'w')
fw.write('Här testas det mmmm')
fw.close()

fr = open('tester.txt', 'r')
text = fr.read()
print(text)
fr.close()

data = ds('tester.txt', 'tester.txt')
tupp = data.datasource_conn('tester.txt')
print(tupp)





# bank1 = bank("Nordea")
# try:
#     print(bank1.name)
#     bank1.welcome_menu()
#
# except KeyboardInterrupt:
#     print("Error")
# finally:
#     bank1.update_db()
