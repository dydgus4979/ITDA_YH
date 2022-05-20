price=int(input())
cupon=str(input())

if cupon == 'Cash3000':
  price -= 3000
elif cupon == 'Cash5000':
  price -= 5000
  
print(price)
