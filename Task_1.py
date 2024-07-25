# Password Complexity Checker

''' @khaja Masthan Shaik '''

print("-----------------------------------------------------------------------------------------------")
print("-----------------------------------------------------------------------------------------------")
print("                           .....Hi....")
print("!!!This tool evaluates your password's strength based on length, rendomness, and complexity.!!!")
print("                             How strong is your password?")
print("-----------------------------------------------------------------------------------------------")
print("-----------------------------------------------------------------------------------------------")
print(" ")
password = input("Enter your password: ")               #user can enter the password 

''' Main source code '''

spical_char = ["!","@","#","$","%","*"]
upper_char = any(key.isupper() for key in password)
Lower_char = any(key.islower() for key in password)
Numbers = any(key.isdigit() for key in password)

correct_or_wrong = all([spical_char,upper_char,Lower_char,Numbers])

# condiction loop 
if len(password) > 14 and correct_or_wrong:
  print(" ")
  print("-------------------------------------------------------------------------")
  print(f'             "{password}\" is very Strong password you can use it')
  print("--------------------------------------------------------------------------")
elif len(password) > 10 and len(password) <= 12 and correct_or_wrong:
  print(" ")
  print("-------------------------------------------------------------------------")
  print(f'             "{password}\" is Strong password you can use it')
  print("--------------------------------------------------------------------------")
  print("             >>>>You can use this password secure your account<<<<")
elif len(password) > 8 and len(password) <= 10 and correct_or_wrong:
  print(" ")
  print("-------------------------------------------------------------------------")
  print(f'             "{password}\" is Medium password you can use it')
  print("--------------------------------------------------------------------------")
  print("              >>>> !!!!!!!!!!----Happy-----!!!!!!!!!!!  <<<<")
elif len(password) > 6 and len(password) <= 8 and correct_or_wrong:
  print(" ")
  print("---------------------------------------------------------------------------")
  print(f'             "{password}\" is Weak password you can use it')
  print("--------------------------------------------------------------------------------------------------------------------------------")
  print("        >>>>Create a Long Password with at least 14 characters...<<<<<")
  print("--------------------------------------------------------------------------------------------------------------------------------")
  print(">>>Include a mix of upper case and lowercase numbers and spical characters. That can help you secure you more with attackers..")
  print("---------------------------------------------------------------------------------------------------------------------------------")
else:
  print(" ")
  print("-------------------------------------------------------------------------")
  print(f'             "{password}\" is very weak password you cannot use this password It is not secure')
  print("!!!! Make sure you will change this password. !!!!")
