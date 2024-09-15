print("hola mundo")
a = 16
print(a)
a = "pepe"
print(a)

def suma(a,b):
  return a+b
print(suma(1,2))

print(ord("a"))
print(chr(113))

bytearray = bytes ([65, 68, 69, 65])
print(bytearray[2])
print(bytearray)

c=input("Introdueix una paraula: ")
def codificar(i):
  r = i+" = "
  for d in c :
    n = ord(d)+1
    m=chr(n)
    r= r+m
  return r

h = codificar(c) 
print(h)
