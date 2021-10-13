File1 = 'сравнение.txt'
File2 = 'бд_новая.txt'

with open(File1,'r', encoding="utf-8") as f:
        d=set(f.readlines())

with open(File2,'r', encoding="utf-8") as f:
        e=set(f.readlines())

with open('сравнение5.txt','a', encoding="utf-8") as f:
        for line in list(e-d):
           print(line) 
           f.write(line)