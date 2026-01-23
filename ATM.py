

#هنا قائمة العملاء الموجودين 
users={} 



def withdraw(name_user):
    amunt=float(input('Enter the amunt:'))
    if amunt <= 0:
        print('ERROR THE AMUNT IS CAN NOT BE <= ZERO')
        return
    if amunt >users[name_user]['balance']:
       print('ERROR : invalid amunt')
       return

    if amunt<=users[name_user]['balance']:
        users[name_user]['balance'] -= amunt
        print('Done')
        users[name_user]['transactions'].append(f'withdraw, {amunt}')

    
def deposit(name_user):
    amunt=float(input('Enter the amunt:'))
    users[name_user]['balance'] += amunt
    print('Done')
    users[name_user]['transactions'].append(f'deposit, {amunt}')

def transactions(name_user):     
    print(users[name_user]['transactions'])
    print('Done')

def balance(name_user):
    print(users[name_user]['balance'])
    print('Done')

#هنا بداية البرنامج 
print('Wellcome to ATM')
name_user=input('Enter the user name :')

if name_user not in users:    #اذا كان العميل غير موجود 
   print('you are new user , create account')
   password=input('create your password:')
   users[name_user]={'password':password,'balance':0,'transactions':[]}
   print('create account is done')

else:
   password=input('Enter your password here: ')
   if password!=users[name_user]['password']:
      print('the password is not correct')
      exit()
while True:
    
      #اختيار العميل العمليه المراده من القائمه
      print('1 - withdraw')
      print('2 - deposit')
      print('3 - show transactions')
      print('4 - show balance')
      print('5 - change my password')
      print('6 - Exit')
      choice=input('Enter your choice:')
      if choice =='1':
        withdraw(name_user)
      if choice=='2':
        deposit(name_user)
      if choice=='3':
        transactions(name_user)
      if choice=='4':
        balance(name_user)
      if choice=='5':
         new_password=input('Enter the new password here:')
         users[name_user]['password']=new_password
         print('Done')
      if choice=='6':
        print('good bay!!!')
        break



