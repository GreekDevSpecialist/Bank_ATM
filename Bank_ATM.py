from sys import exit

class BankATM():
    def __init__(self,username,password,account_balance):
        self._username = username.upper() #Username should inserted with UPPERCASE else it is aborted
        self._password = password
        self._account_balance = account_balance
        self._reports = []


    def account_access(self):
        """This function asks the account holder to insert his username and password.
        Also checks if the credentials were inserted properly and exits after 3 unsuccessful attempts"""
        i = 3
        temp_username = 0
        temp_password = 0
        check = True
        while check: #Checks if username is inserted properly
            temp_username = input('Username: ')
            if temp_username == self._username:
                while i>0:
                    temp_password = input('Password: ')
                    if temp_password == self._password: #Checks if password is inserted properly
                      self.get_menu()
                      check = False #If password is correct, while loop is terminated
                      break
                    else:
                        print ("Password is invalid. Attempts remaining: {0}".format(i-1))
                        i-=1
                        if i == 0: #If password is wrong after 3 attempts, program is terminated
                            print ("Your account is temporary blocked. Exiting...")
                            exit()
            else:
              print ("Your credentials are not correct. Please try again")

    def get_menu(self):
        """This function prints menu on screen by using a dictionary.
        Also asks the user to insert his choice and calls the appropriate function based on user's choice"""
        choice = 0
        times = 5
        print ("Please enter a valid number (1-5):") #Menu is created as dictionary
        menu = {
        1: "Check your account balance ",
        2: "Withdraw Funds ",
        3: "Deposit Funds ",
        4: "Reports ",
        5: "Exit "
        }

		#Prints Menu on screen with this format -> key: value
        print ("#--------------------------------#")
        for keys,values in menu.items():
          print (keys, ':', values)
        print ("#--------------------------------#")

        
        for i in range(0,6):# 5 attempts are allowed for the user. Else program is terminated
          choice = input(" ")
          if choice == '1':
            self.account_balance() #Calls function to check account_balance
            break
          elif choice == '2':
            if self._account_balance >=10:
              self.withdraw_funds() #Calls function to withdraw money
              break
            else:
              print ("Your account balance has less than 10 USD!")
              print ("*** Deposit some money ***")
              self.get_menu()
          elif choice == '3':
            self.deposit_funds() #Calls function to deposit_money
            break
          elif choice == '4':
              """ This choice allows the user to check his last transactions.
              If the transactions are less than 5, then all of them are shown on screen.
              If he made more than 5 transactions, only the last 5 ones are shown on screen"""
              if len(self._reports) <= 5:
                print("Your Account Transactions are listed below: ")
                for i in self._reports:
                    print (i),
              else:
                print("Your Last 5 Account Transactions are listed below: ")
                for i in range(len(self._reports)-5,len(self._reports)):
                    print(self._reports[i]),
              print("\n")
              self.get_menu()
          elif choice == '5':
            exit()
          else:
            if (times-i) >= 1: #Examines the invalid selection
              print ('Your choice is invalid.')
              print ('You have {0} times to try'.format(times-i))
            else:
              print ('Try again later...') #exits program
              exit()
 
    def account_balance(self): #Getting the account's balance
        print ("Your account balance is: ") 
        print ("------> {0} USD <------".format(self._account_balance))
        self.get_menu()
        

    def withdraw_funds(self):
      """This functons checks if there are enough money in the account in order to allow
      the user to withdraw money. If there are, then allows him to withdraw the amount he asked"""
      while True:
        funds_withd = input('How much money you want to withdraw: ')
        if int(funds_withd) > self._account_balance:
          print ('Not sufficient funds. Withdraw less money!')
        else:
          self._account_balance -= int(funds_withd)
          print ("Your updated account balance is:")
          print ("------> {0} USD <------".format(self._account_balance))
          self._reports.append("(%%%%%%%% You Withdraw: {0} USD %%%%%%%%)".format(str(funds_withd)))
          self.get_menu() #Call get_menu until user exits the program
          break

    def deposit_funds(self): #This function deposits money in the account
        funds_depot = input('How much money you want to deposit: ')
        self._account_balance += int(funds_depot)
        print ("Your updated account balance is:")
        print ("------> {0} USD <------".format(self._account_balance))
        self._reports.append("(######## You Deposit: {0} USD ########)".format(str(funds_depot)))
        self.get_menu() #Call get_menu again until he exits

#Initialization: Username: VASILIS / Password: #55aaBB / Account_Balance: 5000 USD
vas_account = BankATM('Vasilis','#55aaBB',5000)
vas_account.account_access()