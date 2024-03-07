def calcular_precio_con_descuento(categoria, precio):
    descuentos = {
        'Ferretería': 0.10,
        'Aseo': 0.05,
        'Seguridad': 0.15,
        'Alimentos': 0.08,
        'Electrodomésticos': 0.12
    }
    if categoria in descuentos:
        tasa_descuento = descuentos[categoria]
        precio_con_descuento = precio * (1 - tasa_descuento)
        return precio_con_descuento
    else:
        return precio  # Sin descuento si la categoría no se encuentra

def principal():
    totales_por_categoria = {
        'Ferretería': 0,
        'Aseo': 0,
        'Seguridad': 0,
        'Alimentos': 0,
        'Electrodomésticos': 0
    }
    total_recaudado = 0

    while True:
        print("Menú:")
        print("1. Agregar Producto")
        print("2. Terminar")

        opcion = input("Ingrese su opción (1 o 2): ")

        if opcion == '1':
            categoria = input("Ingrese la categoría del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            if categoria in totales_por_categoria:
                precio_con_descuento = calcular_precio_con_descuento(categoria, precio)
                totales_por_categoria[categoria] += precio_con_descuento
                total_recaudado += precio_con_descuento
                print("¡Producto agregado exitosamente!\n")
            else:
                print("Categoría inválida. Producto no agregado.\n")
        elif opcion == '2':
            print("Resumen:")
            for categoria, total in totales_por_categoria.items():
                print(f"{categoria}: {total}")
            print(f"Total recaudado: {total_recaudado}")
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Por favor, ingrese 1 o 2.\n")

principal()
