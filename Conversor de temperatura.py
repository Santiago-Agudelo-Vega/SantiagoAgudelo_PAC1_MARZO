def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def principal():
    while True:
        print("Menú:")
        print("1. Celsius a Fahrenheit")
        print("2. Fahrenheit a Celsius")
        print("3. Finalizar")

        opcion = input("Ingrese su opción (1, 2 o 3): ")

        if opcion == '1':
            celsius = float(input("Ingrese la temperatura en Celsius: "))
            fahrenheit = celsius_a_fahrenheit(celsius)
            print(f"{celsius} Celsius es igual a {fahrenheit} Fahrenheit\n")
        elif opcion == '2':
            fahrenheit = float(input("Ingrese la temperatura en Fahrenheit: "))
            celsius = fahrenheit_a_celsius(fahrenheit)
            print(f"{fahrenheit} Fahrenheit es igual a {celsius} Celsius\n")
        elif opcion == '3':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, ingrese 1, 2 o 3.\n")

principal()

        
            

            
            
    
        
        
    

    
    