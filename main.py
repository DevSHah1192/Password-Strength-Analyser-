print(" Welcome To Password Strength Analyser Tool in Python.")
name=input(" Enter Your Good Name :- ")
print(" Hello ",name, " Welcome to Password Strength Analyser.")

print(" Note Your Password Should Contain Following Characters - ")
print(" Password length Min 8 , Max 20. ")
print(" At least Contain One Uppercase. ")
print(" At least Contain One Lowercase. ")
print(" At least Contain One Special Character. ")

points = 0
missing = []

password=input(" Enter Your Password - ")
print(password)

if len(password) >= 8:
     
    print(" Password Length condition meet.")
else:
        print(" Password Length Should be Greater Then [8] Characters. ")
        
        
        
has_upper = False

for ch in password:
    if ch.isupper():
        has_upper = True
        
        break
        
    if not has_upper:
        missing.append(" Need At least One Uppercase Letter.")
        break

has_lower = False
for ch in password:
    if ch.islower():
        has_lower= True
    
        break
    
if not has_lower:
   missing.append(" Need an Lower Case Chracter. ")
    
    
has_digit = False
for ch in password:
    if ch.isdigit():
        has_digit = True
         
        break

if not has_digit:
    missing.append("Need atleast One Digit. ")


special_chars="@#$^&*"
has_special = False
for ch in password:
    if ch in special_chars:
     has_special = True
    
    break

if not has_special:
    missing.append(" Need At least One Special Character. ")
    
    
if len(password) >= 8:
    points+=1
    
if has_upper:
    points+=1

if has_lower:
    points+=1
    
if has_digit:
    points+=1
    
if has_special:
    points+=1
    
print(" Your Password get ",points,"Points ")
    
if missing:
    print(" Missing Condtions not make Your Password Strong is . ")
    for item in missing:
     print("-",item)
     
else:
    print(" All Condition Meets. ")



print("Thanks For Using Strong Password Analyser Please Give Your Feedback. ")

    
