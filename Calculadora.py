num1 = int(input("eligue un valor a operar"))
num2 = int(input("eligue un segundo valor a operar"))

opciones = 0

while opciones!= 6:
    print("""
          indique la operacion deseada:
          
          1) Suma
          2) Resta
          3) Multiplicacion
          4) DIvision
          5) Cambiar valores
          6) Salir
          """)
    opciones = int(input())
    
    if opciones == 1:
        print(" ")
        print("Resultado = ", num1, "+", num2,"=", num1+num2)
        
    if opciones == 2:
        print(" ")
        print("Resultado = ", num1, "-", num2,"=", num1-num2)
        
    if opciones == 3:
        print(" ")
        print("Resultado = ", num1, "x", num2,"=", num1*num2)
        
    if opciones == 4:
        print(" ")
        print("Resultado = ", num1, "/", num2,"=", num1/num2)
        
    if opciones == 5:
        num1 = int(input("eligue un valor a operar"))
        num2 = int(input("eligue un segundo valor a operar"))
        
    if opciones == 6:
        print("Calculadora cerrada")
        