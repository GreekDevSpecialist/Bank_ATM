from sys import exit

class BankATM():
    def __init__(self,username,password,account_balance):
        self._username = username.upper()
        self._password = password
        self._account_balance = account_balance
    
    def account_access(self):
        i = 0
        temp_username = 0
        temp_password = 0
        check = True
        while check:
            temp_username = input('Username: ')
            if temp_username == self._username:
                while i<=3:
                    temp_password = input('Password: ')
                    if temp_password == self._password:
                      self.get_menu()
                      check = False
                      break
                    else:
                        print ("Password is invalid, please try again")
                        i+=1
            else:
              print ("Your credentials are not correct. Please try again")    

    def get_menu(self):
        choice = 0
        times = 5
        menu = {
        1: "Check your account balance ",
        2: "Withdraw Funds ",
        3: "Deposit Funds ",
        4: "Exit "
        }
        
        for keys,values in menu.items():
          print (keys, ':', values)
        
        for i in range(0,6):
          choice = input("Please enter a valid number (1-4): ")
          if choice == '1':
            self.account_balance()
            break
          elif choice == '2':
            if self._account_balance >=10:
              self.withdraw_funds()
              break
            else:
              print ("Your account balance has less than 10 USD!")
              print ("Not sufficient amount to withdraw")
          elif choice == '3':
            self.deposit_funds()
            break
          elif choice == '4':
            exit()
          else:
            if (times-i) >= 1:
              print ('Your choice is invalid.')
              print ('You have {0} times to try'.format(times-i))
            else:
              print ('Try again later...')
 
    def account_balance(self):
        print("Getting account balance")
        print (self._account_balance)
        self.get_menu()
        

    def withdraw_funds(self):
      while True:
        funds_withd = input('How much money you want to withdraw: ')
        if int(funds_withd) > self._account_balance:
          print ('Not sufficient funds. Withdraw less money!')
        else:
          self._account_balance -= int(funds_withd)
          print ("Your new account balance is {0}".format(self._account_balance))
          self.get_menu()
          break

    def deposit_funds(self):
        funds_depot = input('How much money you want to deposit: ')
        self._account_balance += int(funds_depot)
        print ("Your new account balance is {0}".format(self._account_balance))
        self.get_menu()

my_atm = BankATM('Vasilis','#55aaBB',5000)
my_atm.account_access()
