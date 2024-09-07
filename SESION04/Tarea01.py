/*
 * Crea un programa que realize el cifrado César de un texto y lo imprima.
 * También debe ser capaz de descifrarlo cuando así se lo indiquemos.
 *
 * Te recomiendo que busques información para conocer en profundidad cómo
 * realizar el cifrado. Esto también forma parte del reto.
 */

   #Michael Steven Taborda Ceron 
   #Cifrado cesar 
def cifrado_cesar(texto, desplazamiento, modo='cifrar'):

  resultado = ""
  for caracter in texto:
    if caracter.isalpha():
      
      caracter = caracter.lower()
      nuevo_indice = ord(caracter) - ord('a') + desplazamiento
      nuevo_indice %= 26
      nuevo_caracter = chr(nuevo_indice + ord('a'))
      if modo == 'descifrar':
        nuevo_caracter = chr(ord(caracter) - ord('a') - desplazamiento + 26) % 26 + ord('a')
      resultado += nuevo_caracter.upper() if caracter.isupper() else nuevo_caracter
    else:
      resultado += caracter

  return resultado

texto_original = "Hola soy Michael"
desplazamiento = 3

texto_cifrado = cifrado_cesar(texto_original, desplazamiento)
print("Texto cifrado:", texto_cifrado)

texto_descifrado = cifrado_cesar(texto_cifrado, desplazamiento, modo='descifrar')
print("Texto descifrado:", texto_descifrado)
      
    
