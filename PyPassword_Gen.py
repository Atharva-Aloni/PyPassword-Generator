import random as rm
letters = [
    'A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 
    'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 
    'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 
    'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 
    'Y', 'y', 'Z', 'z'
]
number =[ 1,2,3,4,5,6,7,8,9,0]

special = [
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', 
    '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', 
    '_', '`', '{', '|', '}', '~'
]
passw = []
print(""" 
                    ..,,;;;;;;,,,,
       .,;'';;,..,;;;,,,,,.''';;,..
    ,,''                    '';;;;,;''
   ;'    ,;@@;'  ,@@;, @@, ';;;@@;,;';.
  ''  ,;@@@@@'  ;@@@@; ''    ;;@@@@@;;;;
     ;;@@@@@;    '''     .,,;;;@@@@@@@;;;
    ;;@@@@@@;           , ';;;@@@@@@@@;;;.
     '';@@@@@,.  ,   .   ',;;;@@@@@@;;;;;;
        .   '';;;;;;;;;,;;;;@@@@@;;' ,.:;'
          ''..,,     ''''    '  .,;'
               ''''''::''''''''
                                   ,;
                                  .;;
                                 ,;;;
                               ,;;;;:
                            ,;@@   .;
                           ;;@@'  ,;
                           ';;, ,;'

""")
print()
print("Welcome to PyPassword Generator......!!!")
for i in range(0,50):
    print('*',end=" ")
print()
s=int(input("How Many character do you want in your password : "))
for i in range(0,50):
    print('*',end=" ")
print()
j=int(input("Enter how many number do you want in your password : "))
for i in range(0,50):
    print('*',end=" ")
print()
z=int(input("Enter how many Special Character do you want in your password : "))
if(j+z<=s):
    t=s-j-z
    while(t>0):
        ch=rm.choice(letters)
        passw.append(ch)
        t-=1
    while(j>0):
          ch=rm.choice(number)
          passw.append(ch)
          j-=1
    while(z>0):
          ch=rm.choice(special)
          passw.append(ch)
          z-=1
else:
    print("Invalid Entries ")
rm.shuffle(passw)    
p=""
while(len(passw)>0):
    ch=rm.choice(passw)
    passw.remove(ch)
    p+=str(ch)

print()
print(f"Your Password : {p}")
        
