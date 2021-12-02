import re

print("----------------------------------------")
print("Hey! Please Sign Up to Access")
print("----------------------------------------")
print("Note!: \n The password is valid if all criteria are met: \n a. Greater than 15 letters \n b. Have at least one capital letter \n c. Have at least one number \n d. Have at least one special character (!@#$%^&*()_+<>)")
print("----------------------------------------")

user_nm = input("Enter your Username: \n> ")
print("----------------------------------------")
pass_wrd = input("Enter your Password: \n> ")
print("----------------------------------------")

err_mes = str
pw = True

while pw:  
    if (len(pass_wrd) < 16):
        err_mes = 'Password length should be greater than 15 characters.'
        break
    elif not re.search("[a-z]",pass_wrd):
        err_mes = 'Password should have at least one small letter.'
        break
    elif not re.search("[0-9]",pass_wrd):
        err_mes = 'Password should have at least one number.'
        break
    elif not re.search("[A-Z]",pass_wrd):
        err_mes = 'Password should have at least one capital letter.'
        break
    elif not re.search("[!@#$%^&*()_+<>]",pass_wrd):
        err_mes = 'Password should have at least one special character.'
        break
    else:
        print("Valid Password")
        print("Successfully Signed Up.")
        pw=False
        break