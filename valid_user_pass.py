user = input("Enter with your user!\n")
password = input("Enter with your password\n")
while(True):
	if user == password:
		print("Password and User must be different")
		print("Enter with a password again")
		password = input("Enter with your password\n")
		continue
	print("Password correct")
	break

print("User is: ", user)
print("Passowrd is: ", password)

