#POS
#but first coffee

total = 0
menu = [
	['[1] Americano  70',70],
	['[2] Latte  120',120],
	['[3] Mocha  150',150],
	['[4] Fries  80',80],
	['[5] Burger  150',150]
]
print("created by: Lois Cheney Brofar")
print("BUT FIRST, COFFEE <3")
def menuList():
	global total
	print("\nMenu List")
	for i in menu:
		print(i[0])
	sel = int(input('\nPlease choose your order:\n'))
	qty = int(input('\nplease enter quantity:\n'))
	total = total +(menu[sel-1][1] * qty)
	while True:
		cmd = input('\nadd order?  [y/n]\n')
		if cmd == 'y':
			menuList()
			break
		elif cmd == 'n':
			print(total)
			while True:
				money = float(input('\nenter payment amount:\n'))
				if money < total:
					print('\nInvalid Payment..!\n')
				else:
					print('\nyour total: {:.2f}'.format(total))
					print('\nyour payment: {:.2f}'.format(money))
					print('\nyour change: {:.2f}'.format(money-total))
					print('\nThank you for ordering..!\n')
					break
			break
		else:
			print('\nInvalid Command..!\n')
	
menuList()
