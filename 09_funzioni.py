print('inizio')

# import sys
# print(sys.getrecursionlimit())

def f1():
    print('dentro f1')

def f2():
    print('dentro f2 prima di f1')

def f3(arg):
    print(f'hai chiamato f3 con arg = {arg}')
    print(f'dento f3 testo = {testo}')

def f4(arg):
    print(type(arg))
    arg()

# f1()
# f2()
# f1()
# f2()
testo = 'abcdefghijklmnop'
# f3('pippo')
# f3(testo)

f4(f1)

print('fine')