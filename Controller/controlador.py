import sys
sys.path.insert(0, '/Proyectos/Proyecto-1/View') 
sys.path.insert(0, '/Proyectos/Proyecto-1/Model') 
from data import BaseDatos
from view import Vista_Opciones



class Controlador:
    def __init__(self):
        self.model = BaseDatos('data.db')
        self.model.crear_tabla()

    def iniciar_app(self):
        while True:
            Vista_Opciones.menu()
            opcion = input ("[Opción]->")
            self.procesar_opc(opcion)

    def procesar_opc(self, opcion):
        if opcion =='1':
            self.agregar_producto()
        elif opcion == '2':
            self.ver_producto()
        elif opcion == '3':
            self.eliminar_producto()
        elif opcion =='4':
            self.iniciar_chat()
        elif opcion == '5':
              print("¡Gracias por usar nuestro sistema!")
              exit()
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
    
    def agregar_producto(self):
        codigo,nombre,cantidad = Vista_Opciones.agregar_producto()
        self.model.agregar_productos(codigo,nombre,cantidad)
        Vista_Opciones.mostrar_mensaje("[PRODUCTO AGREGADO.]")
    
    def ver_producto(self):
         productos = self.model.listar_productos()
         Vista_Opciones.mostrar_productos(productos)

    def eliminar_producto(self):
        codigo = Vista_Opciones.eliminar_producto()
        producto_eliminado = self.model.eliminar_productos(codigo)
        if producto_eliminado:
            Vista_Opciones.mostrar_mensaje("[PRODUCTO ELIMINADO]")
        else:
            Vista_Opciones.mostrar_mensaje("[PRODUCTO NO ENCONTRADO.]")

    def iniciar_chat(self):
            Vista_Opciones.iniciar_chat()
            mensajes = [
                {"role": "system", "content": "You are a helpful assistant."},
            ]
            while True:
                entrada_usuario =  Vista_Opciones.obtener_entrada_usuario()
                if entrada_usuario.lower() == 'salir':
                    break
                mensajes.append({"role": "user", "content": entrada_usuario})
                respuesta = self.chat.generar_respuesta(mensajes)
                Vista_Opciones.mostrar_respuesta(respuesta)
                mensajes.append({"role": "assistant", "content": respuesta})