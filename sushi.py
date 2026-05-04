menu = """
1. Pikachu Roll $4500
2. Otaku Roll $5000
3. Pulpo Venenoso Roll $5200
4. Anguila Eléctrica Roll $4800
5. Pedido completo.
"""

while True:
    total_productos = 0

    cont_pikachu_roll = 0
    cont_otaku_roll = 0
    cont_pulpo_venenoso_roll = 0
    cont_anguila_electrica_roll = 0

    subtotal = 0
    descuento = 0
    total = 0

    while True:
        print(menu)
        
        while True:
            try:
                opc = int(input("Ingrese el sushi a agregar: "))
            except ValueError:
                print("Debe ingresar un numero.")
            else:
                break

        match opc:
            case 1:
                total_productos += 1
                cont_pikachu_roll += 1
                subtotal += 4500
            case 2:
                total_productos += 1
                cont_otaku_roll += 1
                subtotal += 5000
            case 3:
                total_productos += 1
                cont_pulpo_venenoso_roll += 1
                subtotal += 5200
            case 4:
                total_productos += 1
                cont_anguila_electrica_roll += 1
                subtotal += 4800
            case 5:
                break
            case _:
                print("Ingrese una opción correcta.")

    is_descount_code = input("¿Tiene un código de descuento? (s/n): ")

    if is_descount_code.lower() == "s":
        descount_code = input("Ingrese el código de descuento: ")
        
        if descount_code == "soyotaku":
            descuento = subtotal * 0.10
        else:
            print("Código de descuento no válido.")

    total = subtotal - descuento

    print(f"""
    *******************************
    TOTAL PRODUCTOS: {total_productos}
    *******************************
    Pikachu Roll: {cont_pikachu_roll}
    Otaku Roll: {cont_otaku_roll}
    Pulpo Venenoso Roll: {cont_pulpo_venenoso_roll}
    Anguila Eléctrica Roll: {cont_anguila_electrica_roll}
    *******************************
    Subtotal por pagar: ${subtotal}
    Descuento por código: ${descuento} 
    TOTAL: ${total}
    """)
    
    seguir = input("Quiere ingresar otro pedido? (S/N): ")

    if seguir.upper() == "N":
        break