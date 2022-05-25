# print('punto 1.')
# l1 = open('testo1.txt', 'r')
# l2 = open('testo2.txt', 'r')
# s = open('tutto.txt', 'w')

# for r in l1:
#     s.write(r)
# l1.close()

# for r in l2:
#     s.write(r)
# l2.close()
# s.close()

# print('punto 2.')
# l1 = open('testo1.txt', 'r')
# l2 = open('testo2.txt', 'r')
# s = open('pari1.txt', 'w')

# cnt = 1
# for r in l1:
#     if cnt % 2 == 0:
#         s.write(r)
#     cnt += 1
# l1.close()

# cnt = 1
# for r in l2:
#     if cnt % 2 == 0:
#         s.write(r)
#     cnt += 1
# l2.close()
# s.close()

# print('punto 3.')
# s = open('pari2.txt', 'w')

# cnt = 1
# righe1 = []
# righe2 = []
# with open('testo1.txt', 'r') as l1:
#     for r in l1:
#         if cnt % 2 == 0:
#             righe1.append(r)
#         cnt += 1

# cnt = 1
# with open('testo2.txt', 'r') as l2:
#     for r in l2:
#         if cnt % 2 == 0:
#             righe2.append(r)
#         cnt += 1

# cnt = 0
# while cnt < max(len(righe1), len(righe2)):
#     if len(righe1) > cnt:
#         s.write(righe1[cnt])
#     if len(righe2) > cnt:
#         s.write(righe2[cnt])
#     cnt += 1

# s.close()

# print('punto 4.')
# cnt = 1
# trovate = 0
# with open('testo2.txt', 'r') as l1:
#     for r in l1:
#         pos = r.find('nulla')
#         while pos != -1:
#             trovate += 1
#             pos = r.find('nulla', pos + 5)
#         cnt += 1
# print(f' ho trovato la parola nulla {trovate} volte')

# import os

# print('punto 5.')
# os.mkdir('punto_5')
# os.popen('move tutto.txt punto_5')

print('punto 6.')
s = open('numeri.txt', 'w')
cnt = 0
while cnt <= 1000:
    s.write(f'{str(cnt)}\n')
    cnt += 2

print('finito')