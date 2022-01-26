if len(a) < 4:
    self.customers[a[0]] = cust
elif len(a) > 3:
    acc1 = acc(a[3], a[4], a[5])

# if len(a) <=3:
#     self.customers[a[0]] = cust                                                     
if len(a) <= 6:
    self.customers[a[0]] = cust, acc1
elif len(a) < 10:
    self.customers[a[0]] = cust, acc1, acc(a[6], a[7], a[8])
elif len(a) > 10:
    self.customers[a[0]] = cust, acc1, acc(a[6], a[7], a[8]), acc(a[9], a[10], a[11]) 