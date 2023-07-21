ulist=[]
print('''User Authentication application
	1.Sign up
	2.Log In
	3.Delete User
	4.Exit''')
choice=0
while (choice<4):
		choice=int(input("enter choice:"))

		if choice==1:
			user={}
			user['name']=input("enter name:")
			user['pass']=input("enter pass:")
			user['email']=input("enter mail:")
			ulist.append(user)
			
		if choice==2:
			uname=input("enter uname:")
			upass=input("enter upass:")
			for u in ulist:
				if(u['name']==uname):
					if(u['pass']==upass):
						print("Login successfully")
					else:
						print("pASSWORD INcORRECT")
				else:
					print("Wrong username")
				
		if choice==3:
			username=input("enter user whom you want to delete:")
			for u in ulist:
				if u['name']==username:
					ulist.remove(u)
					print("User deleted")