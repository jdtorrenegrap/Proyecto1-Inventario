class Vista_Opciones:

    @staticmethod
    def menu():
        print("---[ INVENTARIOS XYZ.SAS ]---")
        print("""
             [1]-> AGREGAR UN NUEVO PRODUCTO
             [2]-> VER PRODUCTOS.
             [3]-> ELIMINAR PRODUCTO..
             [4]-> CHAT CON IA.
             [5]-> SALIR.
              """)

    @staticmethod
    def agregar_producto():
        codigo = input("[INGRESE EL CÓDIGO DEL PRODUCTO]-> ")
        nombre = input("[INGRESE NOMBRE DEL PRODUCTO]-> ")
        cantidad = int(input("[INGRESE CANTIDAD DISPONIBLE]-> "))
        return codigo, nombre , cantidad

    @staticmethod
    def mostrar_productos(productos):
        for producto in productos:
            print(f"""
                  Código: {producto[1]}, 
                  Nombre: {producto[2]}, 
                  Cantidad: {producto[3]}
                   """)
            
    @staticmethod
    def eliminar_producto():  # Corrige el nombre de la función
        codigo = input("[CÓDIGO DEL PRODUCTO]->")
        return codigo 

    @staticmethod
    def mostrar_mensaje(mensaje):
        print(mensaje)   