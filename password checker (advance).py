def password_checker(a):
    has_digit=False
    for i in a:
       if i.isdigit():
          has_digit=True
    if has_digit:
       has_spc=False
       for i in a:
          if not i.isalnum():
             has_spc=True
       if has_spc:
          print("password is strong ")
       else:
          print("password must consist special character:")
             
    else:
       print("it must contain a number ")
          
enter=input("enter a password :")
while True:
 if len(enter)<8:
    print("password must contain 8 digits")
 else:
    password_checker(enter)
    break