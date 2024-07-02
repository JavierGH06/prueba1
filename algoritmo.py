texto= "Hello World"
shift=3

def caesar(texto, shift):
 for char in texto.lower():
     alfabeto= "abcdefghijklmnñopqrstuvwxyz"
     encrypted_text= " "
     if char == encrypted_text:
         encrypted_text += char
     index= alfabeto.find(char)
     new_index= index + shift
     print("your text:", char , "number:" , new_index)
     
caesar(texto, shift)