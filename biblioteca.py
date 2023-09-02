#hola
class main:
    def menu_principal(self):
        print("""
                **********
                   MENÚ
                **********
                1) Libros
                2) Autores
                3) Biblioteca
                4) Salir
            """)
        self.opciones()
        
    def opciones(self):
        fin=False
        while not (fin):
            op = int(input("Ingrese el número de la opción deseada: "))
            if op == 1:
                self.menu_libros()
            elif op == 2:
                self.menu_autores()
            elif op == 3:
                self.menu_biblioteca()
            elif op == 4:
                exit()
        
    def menu_libros(self):
        print("""
                **********
                  LIBROS
                **********
                1) Agregar libro
                2) Editar libro
                3) Mostrar libros
                4) Salir
            """)
        fin = False
        while not(fin):
            op = int(input("Ingrese el número de la opción deseada: "))
            if op == 1:
                print("Agregando...")
            elif op == 2:
                print("Editando...")
            elif op == 3:
                print("Mostrando...")
            elif op == 4:
                self.menu_principal()
                
    def menu_autores(self):
        print("""
                **********
                  AUTORES
                **********
                1) Agregar autor
                2) Editar autor
                3) Mostrar autor
                4) Salir
            """)
        fin = False
        while not(fin):
            op = int(input("Ingrese el número de la opción deseada: "))
            if op == 1:
                print("Agregando...")
            elif op == 2:
                print("Editando...")
            elif op == 3:
                print("Mostrando...")
            elif op == 4:
                self.menu_principal()
                
    def menu_biblioteca(self):
        print("""
                ************
                 BIBLIOTECA
                ************
                1) Mostrar
                2) Salir
            """)
        fin = False
        while not(fin):
            op = int(input("Ingrese el número de la opción deseada: "))
            if op == 1:
                print("Mostrando")
            elif op == 2:
                self.menu_principal()


menu = main()
menu.menu_principal()

#---------------clase de autores----------------
class Autores:
    def __init__(self):
        self.autores = []
    
    def agregarautor(self):
        nombre = input("Ingresar el nombre del autor: ")
        apellido = input("Ingresar el apellido del autor: ")
        self.autores.append({'Nombres': nombre, 'Apellido': apellido})
    
    def mostrarautor(self):
        for i in range(len(self.autores)):
            print("+-------------------------------------------------+")
            print("|                Datos del autor                  |")
            print("+-------------------------------------------------+")
            print("| Nombre:   ","{:<36}".format(self.autores[i]['Nombres']),"|")
            print("| Apellido: ", "{:<36}".format(self.autores[i]['Apellido']),"|")
            print("+-------------------------------------------------+")


    def buscar_autor(self, nombre_buscar):
        for bautor in self.autores:
            if bautor['Nombres'] or bautor['Apellido'] == nombre_buscar:
                return bautor
        return None
    
    def editar_autor(self, autor_encontrado):
        print("1. Modificar nombre del autor")
        print("2. Modificar apellido del autor")
        print("3. Modificar ambos")
        print("4. Salir")
        seleccion = int(input("Seleccionar una opción: "))
        if seleccion == 1:
            nuevo_nombre = input("Ingrese el nuevo nombre: ")
            autor_encontrado['Nombres'] = nuevo_nombre
            print("Nombre modificado")
        elif seleccion == 2:
            nuevo_apellido = input("Ingrese el nuevo apellido: ")
            autor_encontrado['Apellido'] = nuevo_apellido
            print("Apellido modificado")
        elif seleccion == 3:            
            nuevo_nombre = input("Nuevo nombre: ")
            nuevo_apellido = input("Nuevo apellido: ")
            autor_encontrado['Nombres'] = nuevo_nombre
            autor_encontrado['Apellido'] = nuevo_apellido
            print("El nombre completo fue modificado.")
        elif seleccion == 4:
            print("")
        else:
            print("seleccion incorrecta, intente nuevamente")
            
            
    
autor = Autores()

while True:
    print("1. Agregar autor")
    print("2. Mostrar autores")
    print("3. Buscar y editar autor")
    print("4. Salir")
    
    opcion = int(input("Seleccionar una opción: "))
    
    if opcion == 1:
        autor.agregarautor()
    elif opcion == 2:
        autor.mostrarautor()
    elif opcion == 3:
        nombre_buscar = input("Ingrese el nombre o apellido del autor a buscar y editar: ")
        autor_encontrado = autor.buscar_autor(nombre_buscar)
        if autor_encontrado:
            autor.editar_autor(autor_encontrado)
        else:
            print("Autor no encontrado.")
    elif opcion == 4:
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")

#---------------- clase de libros