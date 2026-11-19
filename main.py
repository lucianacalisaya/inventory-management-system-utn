# Trabajo Práctico Integrador: Sistema de Control de Inventario
# Programación 1
# Tecnicatura Universitaria en Programación a Distancia
# Alumna: Calisaya, Luciana

"""Programa principal del Sistema de Control de Inventario,
Este es el archivo que se ejecuta para iniciar el sistema: python main.py
Importa las funciones de las opciones del menú desde funciones.py
"""

from funciones import (
    mostrar_menu,
    leer_entero,
    cargar_herramientas,
    visualizar_inventario,
    consultar_stock,
    reporte_agotados,
    alta_producto,
    actualizar_stock,
)

def main():
    """Crea el inventario y repite el menú hasta que se elige la opción 7 [Salir].
    El ``except`` recibe los errores de la opción inválida (no entera o fuera de rango)
    y los que salen sin capturar de las opciones 3, 5 y 6; muestra el motivo y el menú vuelve a mostrarse.
    """

    inventario = []
    opcion = 0
    while opcion != 7:
        mostrar_menu()
        try:
            opcion = leer_entero("Seleccione una opción: ")
            if opcion == 1:
                cargar_herramientas(inventario)
            elif opcion == 2:
                visualizar_inventario(inventario)
            elif opcion == 3:
                consultar_stock(inventario)
            elif opcion == 4:
                reporte_agotados(inventario)
            elif opcion == 5:
                alta_producto(inventario)
            elif opcion == 6:
                actualizar_stock(inventario)
            elif opcion != 7:
                raise ValueError("Opción fuera de rango (1 a 7).")
        except ValueError as e:
            print(f"Error: {e}")
    print("Sistema Finalizado. Hasta luego!")

if __name__ == "__main__":

    print("\n" + "=" * 62)
    print("       Trabajo Práctico Integrador - Sistema de Control de Inventario")
    print("       Programación 1")
    print("       Tecnicatura Universitaria en Programación a Distancia")
    print("       Alumna: Calisaya, Luciana")
    print("=" * 62)

    main()