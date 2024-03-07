def contar_vocales(cadena):
    # Paso 1: Inicializar contadores para cada vocal y el conteo total
    conteo_vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    conteo_total = 0
    
    # Paso 2: Repetir a través de cada caracter en la cadena de entrada
    for caracter in cadena.lower():
        
        # Paso 3: Verificar si el caracter es una vocal
        if caracter in conteo_vocales:
            
            # Paso 4: Incrementar el contador
            conteo_vocales[caracter] += 1
            conteo_total += 1
    
    # Paso 5: Mostrar el conteo de cada vocal y el conteo total
    for vocal, conteo in conteo_vocales.items():
        print(f"Cantidad de '{vocal}': {conteo}")
    print("Conteo total de vocales:", conteo_total)

# Paso 6: Programa principal
while True:
    entrada_usuario = input("Ingrese un valor(escriba 'finalizar' para detenerse):")
    if entrada_usuario.lower() == 'finalizar':
        break

contar_vocales(entrada_usuario)

        
    

    
    