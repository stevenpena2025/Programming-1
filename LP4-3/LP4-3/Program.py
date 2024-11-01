print "Hello, World!"
eggs = int(input("Enter # of eggs calculate:"))
price = 0.0
cost = 0.0 
dozens = eggs // 12
remainder = eggs % 12 

if eggs >0 and eggs <= 4:
    price = 0.50 

elif eggs >4 and eggs <= 6:
    price = 0.45
    
elif eggs >6 and eggs <= 11:
    price = 0.40
    
elif eggs <11:
    price = 0.35

elif eggs <12:
    price = dozen - remainder
    pass
    
elif eggs <12:
    price = dozen - 12 





cost = eggs * price

print("Price per egg is $" + str(price))
print("Total Cost is $" + str(round(cost,2)))
input()#Press 'Enter' to close

