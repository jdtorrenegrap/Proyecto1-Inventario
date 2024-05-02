import sys
sys.path.insert(0, '/Proyectos/Proyecto-1/View') 
sys.path.insert(0, '/Proyectos/Proyecto-1/Model')
from data import BaseDatos
from view import Vista_Opciones
import asyncio



class Controlador:
    """Controlador para la aplicación de gestión de productos."""

    def __init__(self):
        """Inicializa el controlador con una base de datos."""
        self.model = BaseDatos('data.db')
        self.model.crear_tabla()    

    def iniciar_app(self):
        """Inicia la aplicación."""
        while True:
            Vista_Opciones.menu()
            opcion = input ("[Opción]->")
            if opcion == '5':
                print("¡Gracias por usar nuestro sistema!")
                break
            asyncio.run(self.procesar_opcion(opcion))

    async def procesar_opcion(self, opcion):
        """Procesa la opción seleccionada por el usuario."""
        if opcion =='1':
           await self.agregar_producto()
        elif opcion == '2':
            self.ver_producto()
        elif opcion == '3':
            self.eliminar_producto()
        elif opcion =='4':
            self.iniciar_chat()
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

    async def agregar_producto(self):
        """Agrega un producto a la base de datos."""
        n= int(input("Productos a agregar ->"))
        for i in range(n):
            codigo, nombre, cantidad = Vista_Opciones.agregar_producto()
            await asyncio.sleep(1)
            Vista_Opciones.mostrar_mensaje("[REALIZANDO PROCESO..]")
            self.model.agregar_productos(codigo, nombre, cantidad)
            Vista_Opciones.mostrar_mensaje("[PRODUCTO AGREGADO.]")
    
    def ver_producto(self):
        """Muestra los productos en la base de datos."""
        productos = self.model.listar_productos()
        Vista_Opciones.mostrar_productos(productos)

    def eliminar_producto(self):
        """Elimina un producto de la base de datos."""
        codigo = Vista_Opciones.eliminar_producto()
        producto_eliminado = self.model.eliminar_productos(codigo)
        if producto_eliminado:
            Vista_Opciones.mostrar_mensaje("[PRODUCTO ELIMINADO]")
        else:
            Vista_Opciones.mostrar_mensaje("[PRODUCTO NO ENCONTRADO.]")

    def iniciar_chat(self):
        """Inicia el chat."""
        Vista_Opciones.mostrar_mensaje("¡Estamos trabajando en una nueva función! ¡Pronto estará disponible!")