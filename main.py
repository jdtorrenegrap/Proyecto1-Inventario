import sys
sys.path.insert(0, '/Proyectos/Proyecto-1/Controller') 
from controlador import Controlador

def main():
    controlador = Controlador()
    controlador.iniciar_app()

if __name__ == "__main__":
    main()