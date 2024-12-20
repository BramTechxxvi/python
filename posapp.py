total = 0

while True:
	menu = int(input("1. Deposit \n2. Withdraw \n3. Exit \n\nSelect an option: "))
	match menu:
		case 1:
			deposit = float(input("Enter deposit Amount: "))
			total += deposit
			print(f"Deposit Succesful \nYour present balance is: {total}")

		case 2: 
			withdraw = float(input("Enter withdrawal Amount: ")) 
			if withdraw > total:
				print("Insufficient funds")
			else:
				total -= withdraw
				print(f"Withdrawal Succesful \nYour new balance is {total}:")
		
		case 3:
			print("THANK YOU!")
			break 
	    
		case _:
			print("Invalid option")

	