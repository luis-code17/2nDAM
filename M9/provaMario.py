'''
f = open("mario_1byte.bmp", "rb+")
#ara afegim 3 bytes

f.seek(1080) #Anem al 1r byte
bytellegit = f.read(1)
print(bytellegit)

f.seek(1081) #Anem al 2n byte
bytellegit = f.read(1)
print(bytellegit)

f.seek(1082) #Anem al 3r byte
bytellegit = f.read(1)
print(bytellegit)


f = open("mario_1byte.bmp", "rb+")
byteFF=bytes.fromhex('FF')
f.seek(1080)
f.write(byteFF)
f.seek(1081)
f.write(byteFF)
f.seek(1082)
f.write(byteFF)
f.close()

exit(0)
'''

f = open("mario_1byte.bmp", "rb+")
byteFF=bytes.fromhex('FF')
for i in range(1080,1000000):
  f.seek(i)
  f.write(byteFF)


