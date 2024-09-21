
print(ord("a"))
def encrypt(word):
    result = word+" = "

    for character in word :
      numCharacter = ord(character)+1
      newCharacter=chr(numCharacter)
      result= result+newCharacter

    return result
 
def decipher(word):
  result = word+" = "

  for character in word :
      numCharacter = ord(character)-1
      newCharacter=chr(numCharacter)
      result= result+newCharacter

  return result

scanner = input("que vols? codificar(1) o descodificar(2) ")
if scanner == "1":
  scanner2 = input("Introdueix una paraula: ")
  newNum = encrypt(scanner2) 
  print(newNum)
elif scanner== "2":
    scanner2 = input("Introdueix una paraula: ")
    newWord = decipher(scanner2) 
    print(newWord)
   
