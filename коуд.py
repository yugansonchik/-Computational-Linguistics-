import sys
n = input()
b = input()
true1 = 0
true2 = 0
true3 = 0
true4 = 0

for i in range(len(n)):
    if "0" <= n[i] <= "9":
        sys.exit('Wrong input')
    else:
        if "a" <= n[i] <= "z" or "A" <= n[i] <= "Z":
            true1+= 1
        elif 'à' <= n[i] <= 'ÿ' or 'À' <= n[i] <= "ß":
            true2+= 1
for i in range (len(b)):
    if "0" <= b[i] <= 'g':
        sys.exit('Wrong input')
    else:
        if "a" <= b[i] <= "z" or "A" <= b[i] <= "Z":
            true3+=1
        elif 'a' <= b[i] <= 'ÿ' or 'À' <= b[i] <= "ß":
            true4+=1 
            
if true1 == len(n) and true4 == len(b):
    print("English word is", n)
    print("Russian word is", b)
elif true2 == len(n) and true3 == len(b):
    print("English word is", b)
    print("Russian word is", n)
else:
    print("Wrong")
    