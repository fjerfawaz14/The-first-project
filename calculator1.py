History=[]
while True:
    print("*** Wellcome to my calculator!!! ***")
    print("what your choice ?")
    print("1 - Addition " )
    print("2 - Subtraction " )
    print("3 - Multiplication " )
    print("4 - Division" )
    print("5 - modulus " )
    print("6 - exponent " )
    print('7 - show my history')
    print('8 - Exit')
    choice=input("Enter your choic here pleas:")

    try:
     num1=float(input('Enter the first number here:'))
     num2=float(input("Enter the second number here:"))
    except:
      print('ERROR: pleas enter vaild number')
      continue
    


    if choice=="1":
        result1=num1+num2
        print(f'The result is:{num1} + {num2} = {result1}')
        History.append(f'The result is:{num1} + {num2} = {result1}')
    elif choice=='2':
        result2=num1-num2
        History.append(f'The result is: {num1} - {num2} = { result2}')
        print(f'The result is: {num1} - {num2} = { result2}')
    elif choice=='3':
        result3=num1*num2
        History.append(f'The result is:{num1} * {num2}  = {result3}')
        print(f'The result is:{num1} * {num2}  = {result3}')
    elif choice=='4':
        if num2==0:
         print('number error')
        else:
          result4=num1/num2
          History.append(f'The result is:{num1} /{num2} ={result4}')
          print(f'The result is:{num1} /{num2} ={result4}')
    elif choice=='5':
        if num2==0:
           print('ERROR')
        else:
         result5=num1%num2
         History.append(f'The result is:{num1}%{num2}={result5}')
         print(f'The result is:{num1}%{num2}={result5}')
    elif choice=='6':
        result6=num1**num2
        History.append(f'The result is:{num1}**{num2}={ result6}')
        print(f'The result is:{num1}**{num2}={ result6}')
    elif choice=='7':
       if len(History)==0:
          print('no opprations yet')
       else:
         for item in History:
              print(item)
         continue
    elif choice=='8':
       print('good bay')
       break
    else:
        print('ERROR')