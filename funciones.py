#----------------------------------------------
# Funciones auxiliares
#----------------------------------------------

def mostrar_menu():
    """Imprime en pantalla el menú principal con las 7 opciones disponibles."""

    print()
    print("===== CONTROL DE INVENTARIO - FERRETERÍA =====")
    print("1. Cargar herramientas con existencias iniciales")
    print("2. Visualización de inventario")
    print("3. Consultar stock")
    print("4. Reporte de agotados")
    print("5. Alta de nuevo producto")
    print("6. Actualizar stock (venta / ingreso)")
    print("7. Salir")

def leer_entero(mensaje):
    """Pide un dato por teclado y lo convierte a un número entero.
    Si el texto ingresado no se puede convertir, captura el ValueError de int()
    y lo lanza de nuevo con un mensaje claro.
    """

    try:
        return int(input(mensaje))
    except ValueError:
        raise ValueError("Debe ingresar un número entero (sin decimales ni letras).")
    
def validar_nombre(nombre):
    """Valida que un nombre no esté vacío ni formado sólo por espacios."""

    nombre = nombre.strip()
    if nombre == "":
        raise ValueError("El nombre de la herramienta no puede estar vacío.")
    return nombre

def buscar_herramienta(inventario, nombre):
    """Busca una herramienta en el inventario por su nombre."""

    nombre_buscado = nombre.strip().lower()
    for producto in inventario:
        if producto["herramienta"].lower() == nombre_buscado:
            return producto
    return None

def leer_nombre_nuevo(inventario):
    """Pide el nombre de una herramienta nueva y lo valida."""

    nombre = validar_nombre(input("Nombre de la herramienta: "))
    if buscar_herramienta(inventario, nombre) is not None:
        raise ValueError(f"La herramienta '{nombre}' ya existe en el inventario.")
    return nombre

def leer_stock_inicial():
    """Pide el stock inicial de una herramienta y lo valida."""

    stock = leer_entero("Stock inicial: ")
    if stock < 0:
        raise ValueError("El stock inicial no puede ser negativo.")
    return stock

def leer_cantidad_herramientas():
    """Pide cuántas herramientas distintas se van a cargar en la opción 1."""

    cantidad = leer_entero("¿Cuántas herramientas distintas desea cargar? ")
    if cantidad <= 0:
        raise ValueError("La cantidad de herramientas a cargar debe ser mayor que 0.")
    return cantidad

#----------------------------------------------
# Funciones de las opciones del menú
#----------------------------------------------

# Opción 1 - Cargar herramientas
def cargar_herramientas(inventario):
    """Pide cuántas herramientas se van a cargar y por cada una pide su nombre y su stock.
    Los errores se capturan dentro de la función y se vuelve a pedir el dato inválido. Cada
    herramienta se agrega al inventario cuando nombre y stock son válidos.
    """

    cantidad = 0
    while cantidad == 0:
        try:
            cantidad = leer_cantidad_herramientas()
        except ValueError as e:
            print(f"Dato inválido: {e} Intente de nuevo.")

    for numero in range(1, cantidad + 1):
        print(f"----- Herramienta {numero} de {cantidad}. -----")

        nombre = ""
        while nombre == "":
            try: 
                nombre = leer_nombre_nuevo(inventario)
            except ValueError as e:
                print(f"Dato inválido: {e} Intente de nuevo.")

        stock = -1
        while stock < 0:
            try:
                stock = leer_stock_inicial()
            except ValueError as e:
                print(f"Dato inválido: {e} Intente de nuevo.")

        inventario.append({"herramienta": nombre, "cantidad": stock})
        
        print(f"Herramienta '{nombre}' cargada con {stock} unidades.")


# Opción 2 - Visualización del inventario
def visualizar_inventario(inventario):
    """Muestra el listado completo de herramientas y su stock."""

    if len(inventario) == 0:
        print("Todavía no hay herramientas cargadas.")
        return
    
    print("----- Inventario Actual -----")

    for producto in inventario:
        print(f"{producto['herramienta']}: {producto['cantidad']} unidades.")


# Opción 3 - Consulta de Stock
def consultar_stock(inventario):
    """Consulta el stock de una herramienta por su nombre.
    Si no hay herramientas cargadas lo informa sin pedir datos.
    Si el nombre es inválido lanza ValueError.
    """

    if len(inventario) == 0:
        print("Todavía no hay herramientas cargadas.")
        return

    nombre = validar_nombre(input("Nombre de la herramienta a consultar: "))
    producto = buscar_herramienta(inventario, nombre)
    if producto is None:
        print(f"La herramienta '{nombre}' no se encuentra en el inventario.")
    else:
        print(f"{producto['herramienta']}: {producto['cantidad']} unidades disponibles.")


# Opción 4 - Reporte de Agotados
def reporte_agotados(inventario):
    """Muestra las herramientas cuyo stock es 0.
    Distingue 3 casos: inventario vacío, agotados y no agotados.
    """

    if len(inventario) == 0:
        print("Todavía no hay herramientas cargadas.")
        return

    hay_agotados = False
    for producto in inventario:
        if producto["cantidad"] == 0:
            if not hay_agotados:
                print("----- Herramientas agotadas -----")
                hay_agotados = True
            print(f"{producto['herramienta']}: 0 unidades.")        
    
    if not hay_agotados:
        print("Ninguna herramienta tiene stock cero.")


# Opción 5 - Alta de Nuevo Producto
def alta_producto(inventario):
    """Agrega una herramienta nueva al final del inventario.
    Pide primero el nombre y lo valida. Si es válido, pide el stock.
    Si hay errores no se agrega al inventario.
    """

    nombre = leer_nombre_nuevo(inventario)
    stock = leer_stock_inicial()
    inventario.append({"herramienta": nombre, "cantidad": stock})

    print(f"Herramienta '{nombre}' agregada con {stock} unidades.")


# Opción 6 - Actualización de stock (venta / ingreso)
def actualizar_stock(inventario):
    """Registra una venta (resta stock) o un ingreso (suma stock).
    Comprueba que haya herramientas, pide y valida el nombre,
    comprueba existencia, pide el tipo de movimiento, pide y valida
    las unidades, verifica que alcance el stock si es una venta
    y recién ahí modifica el stock. Si algo falla, no se modifica
    el stock.
    """

    if len(inventario) == 0:
        print("Todavía no hay herramientas cargadas.")
        return
    
    nombre = validar_nombre(input("Nombre de la herramienta a modificar: "))
    producto = buscar_herramienta(inventario, nombre)
    if producto is None:
        print(f"La herramienta '{nombre}' no se encuentra en el inventario.")
        return

    print("----- Tipo de movimiento a realizar: 1) Venta 2) Ingreso -----")
    tipo = input("Seleccione el tipo de movimiento: ").strip().lower()
    es_venta = tipo == "1" or tipo == "venta"
    es_ingreso = tipo == "2" or tipo == "ingreso"

    if not es_venta and not es_ingreso:
        print("Tipo de movimiento inválido. Debe ser venta (1) o ingreso (2).")
        return

    unidades = leer_entero("Unidades del movimiento: ")
    if unidades <= 0:
        raise ValueError("Las unidades del movimiento deben ser mayores que 0.")
 
    if es_venta:
        if unidades > producto["cantidad"]:
            raise ValueError(
                f"Stock insuficiente: hay {producto['cantidad']} unidades "
                f"y se intentan vender {unidades}."
            )
        producto["cantidad"] = producto["cantidad"] - unidades
        print(f"Venta registrada. Stock actual de '{producto['herramienta']}': "
              f"{producto['cantidad']}.")
    else:
        producto["cantidad"] = producto["cantidad"] + unidades
        print(f"Ingreso registrado. Stock actual de '{producto['herramienta']}': "
              f"{producto['cantidad']}.")