
def encrypt(nameFile) :
  try:
    with open(nameFile, "rb") as f:  # Solo lectura del archivo original
            
      file_content = f.read()
      encrypted_content = bytearray(file_content)

      for i in range(len(encrypted_content)):
          encrypted_content[i] = (encrypted_content[i] + 1) % 256  # rango válido de 0 a 255.

    newFileName = "COD_" + nameFile
    with open(newFileName, "wb") as fCOD_: #nou arichiu amb el prefix _cod
        fCOD_.write(encrypted_content) #Guardem el text encriptat

    print(f"Archiu '{newFileName}' encriptat amb exit!.")

  except FileNotFoundError:
    print("ERROR: Aquest nom no existeix")

def decipher(nameFile):
  try:
    with open(nameFile, "rb") as f: 
            
      file_content = f.read()
      decipher_content = bytearray(file_content)

      for i in range(len(decipher_content)):
          decipher_content[i] = (decipher_content[i] - 1) % 256  # rango válido de 0 a 255.

      # Crear el nuevo nombre de archivo eliminando el prefijo 'COD_'
      if nameFile.startswith("COD_"):
          newFileName = nameFile.replace("COD_", "DEC_", 1)
      else:
          newFileName = "DEC_" + nameFile

    with open(newFileName, "wb") as fDEC_: #nou arichiu amb el prefix _dec
        fDEC_.write(decipher_content) #Guardem el text encriptat

    print(f"Archiu '{newFileName}' desencriptat amb exit!.")

  except FileNotFoundError:
    print("ERROR: Aquest nom no existeix")



while True:
  action = input("Vols codificar(1), decodificar(2) o sortir(3)? ")

  if action == "1":
      nameFile = input("Digues el nom del arxiu: ")
      encrypt(nameFile)

  elif action == "2":
      nameFile = input("Digues el nom del arxiu: ")
      decipher(nameFile)

  elif action == "3":
      print("Sortint del programa...")
      break

  else:
      print("Acció no vàlida, introdueix 1, 2 o 3.")