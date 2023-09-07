class Libros:
    def __init__(self):
        self.libros = []

    def agregar_libro(self):
        titulo = input("Ingrese el nombre del libro: ")
        anio = int(input("Ingrese el año de edición del libro: "))
        autor = input("Ingrese el nombre del autor: ")
        datos_libro = {'titulo': titulo, 'anio': anio, 'autor': autor}
        self.libros.append(datos_libro)
        print("Los datos fueron guardados correctamente.")

    def busca_libro(self):
        if len in (self.libros) == 0:
            print("No hay libros registrados en la biblioteca.")
        else:
            buscar = input("Ingrese el nombre del libro que desea buscar: ")
            for busca in self.libros:
                if busca['titulo'] == buscar:
                    print("Título: ", busca['titulo'])
                    print("Año: ", busca['anio'])
                    print("Autor: ", busca['autor'])

    def editar_libro(self):
        buscar_libro = input("Ingrese el título que desea modificar: ")
        if len(self.libros) == 0:
            print("No se encontraron libros registrados.")
        else:
            for titulo in self.libros:
                if titulo['titulo'] == buscar_libro:
                    print("Título: ", titulo['titulo'])
                    print("Año: ", titulo['anio'])
                    print("Autor: ", titulo['autor'])
                    opcion = int(input("""¿Que opción desea modificar?:
                                       1-Nombre
                                       2-Autor
                                       3-Año de Edición
                                       Ingrese número de opcion: """))
                    if opcion == 1:
                        nombre = input('Ingrese nuevo nombre:')
                        self.libros[self.libros.index(titulo)]['titulo'] = nombre
                    elif opcion == 2:
                        autor = (input('Ingrese nuevo autor:'))
                        self.libros[self.libros.index(titulo)]['autor'] = autor
                    elif opcion == 3:
                        anio = input('Ingrese nuevo año de edición:')
                        self.libros[self.libros.index(titulo)]['anio'] = anio
                    elif opcion == 4:
                        condicion = True
#-----------Fin de la clase libros--------------
#-----------Comienzo clase biblioteca-----------
class Biblioteca(Libros):
    def mostrar_libros(self):
       print("________Libros registrados________")
       for muestra in self.libros:
            print("_____________________________")
            print("Titulo: ", muestra['titulo'])
            print("Año: ", muestra['anio'])
            print("Autor: ", muestra['autor'])
            print("_____________________________")

#---------------comienzo de clase de autores----------------
class Autores:
    def __init__(self):
        self.autores = []
    
    def agregarautor(self):
        nombre = input("Ingresar el nombre del autor: ")
        apellido = input("Ingresar el apellido del autor: ")
        datos_autores = {'Nombres': nombre, 'Apellido': apellido} 
        self.autores.append(datos_autores)
    
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
    
#-------------------Fin de la clase autores--------------

#--------------inicio de menu-----------------------
class Menu(Biblioteca, Autores):
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
                self.agregar_libro()
                self.menu_libros()
            elif op == 2:
                print("Editando...")
                self.editar_libro()
                self.menu_libros()
            elif op == 3:
                print("Mostrando...")
                self.mostrar_libros()
                self.menu_libros()
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
                self.agregarautor()
                
            elif op == 2:
                print("Editando...")
                self.editar_autor()
                self.menu_autores()
            elif op == 3:
                print("Mostrando...")
                self.mostrarautor()
                self.menu_autores()
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
                self.mostrar_libros()
                self.menu_biblioteca()
            elif op == 2:
                self.menu_principal()
menu = Menu()
menu.menu_principal()
