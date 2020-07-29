import os
print("2nd degree equation Automating solve")
print("just type your 2nd degree equation like this 'ax**2 +/- bx +/- c' (WITH SPACES) the code will consider this "
      "equation is equal to Zero")
equation = str(input("enter your equation here : ")).split(" ")
#print(equation)
if len(equation) != 5:
	print("input not in correct format , input exemple : 8x**2 + 6x - 18")
	print("exiting...")
	exit()
if str(equation[0][-1]) != '2' or equation[2][-1] != 'x' or equation[4][-1].isalpha():
    print("not a 2nd degree equation ! exiting ..."
    "input exemple : 2x**8 + x - 9")
    os.system(exit())

else:
    print("2nd degree equation confirmed ...")

#finding a,b and c numbers
#finding a


def a():
    numb = equation[0].split('x')
    if numb[0] == '':
        return '1'
    else:
        return numb[0]


try:
    print("number 'a' found : {}".format(int(a())))
    a=int(a())
except:
    print("there was an error while finding number 'a' , please make sure of your input ! exiting ...")
    os.system(exit())
#finding b


def b():
    numb = equation[2].split('x')
    if numb[0] == '':
        return equation[1]+'1'
    else:
        number = equation[1]+numb[0]
        return number


try:
    print("number 'b' found : {}".format(int(b())))
    b=int(b())
except:
    print("there was an error while finding number 'b' , please make sure of your input ! exiting ...")
    os.system(exit())

#finding c


def c():
    numb = equation[3]+equation[4]
    return numb


try:
    print("number 'c' found : {}".format(int(c())))
    c=int(c())
except:
    print("there was an error while finding number 'c' , please make sure of your input ! exiting ...")
    os.system(exit())
 # finding Delta

Delta = (b**2) - 4*a*c
#print("Delta found : {}".format(int(Delta)))
if int(Delta) < 0:
    print("this equation has no valid solution ! ( Delta < 0)")
    os.system(exit())

if int(Delta) == 0:
    solution = -b/(2*a)
    print("this equation has only one solution : {}".format(solution))

if int(Delta) > 0:
    import math
    solution1 = (-b + math.sqrt(int(Delta)))/(2*a)
    solution2 = (-b - math.sqrt(int(Delta)))/(2*a)
    print("this equation has 2 solutions : {} and {}".format(solution1,solution2))


print("my discord : Chikasuji#3682") 
os.system("pause")
