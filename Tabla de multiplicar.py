def mostrar_tabla_multiplicar(numero):
    print(f"Tabla de multiplicar de {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
        
def principal():
    while True:
        entrada = input('Ingrese un numero entero positivo: ')
        if entrada.isdigit():
            N = int(entrada)
            if N > 0:
                
                mostrar_tabla_multiplicar(N)
                break
            
        print('Entrada no valida. Por favor, ingrese un numero valido')
        
principal()
        
            

            
            
    
        
        
    

    
    