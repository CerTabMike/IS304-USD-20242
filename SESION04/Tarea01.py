/*
 * Crea un programa que realize el cifrado César de un texto y lo imprima.
 * También debe ser capaz de descifrarlo cuando así se lo indiquemos.
 *
 * Te recomiendo que busques información para conocer en profundidad cómo
 * realizar el cifrado. Esto también forma parte del reto.
 */

def cifrado_cesar(texto, desplazamiento, modo='cifrar'):
  
  resultado = ""
  for caracter in texto:
    if caracter.isalpha():
      
      caracter = caracter.lower()
      
      nuevo_indice = ord(caracter) - ord('a') + desplazamiento
      
      nuevo_indice %= 26
      
      nuevo_caracter = chr(nuevo_indice + ord('a'))
      
    
