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
        while True:
            buscar_libro = input("Ingrese el título que desea modificar: ")
            if len(self.libros) == 0:
                print("No se encontraron libros registrados.")
            else:
                for titulo in self.libros:
                    if titulo['titulo'] == buscar_libro:
                        print("Título:", titulo['titulo'])
                        print("Año:", titulo['anio'])
                        print("Autor:", titulo['autor'])
                        print("************************")
                        print("""
                            ¿Que opción desea modificar?:
                            1-Nombre
                            2-Autor
                            3-Año de Edición
                            """)    
                        opcion = int(input("Ingrese número de opcion: "))
                        if opcion == 1:
                            nombre = input('Ingrese nuevo nombre:')
                            self.libros[self.libros.index(titulo)]['titulo'] = nombre
                            print("Cambios guardados correctamente")
                            return #luego de guardar sale de la funcion 
                        elif opcion == 2:
                            autor = (input('Ingrese nuevo autor:'))
                            self.libros[self.libros.index(titulo)]['autor'] = autor
                            print("Cambios guardados correctamente")
                            return #luego de guardar sale de la funcion                         
                        elif opcion == 3:
                            anio = input('Ingrese nuevo año de edición:')
                            self.libros[self.libros.index(titulo)]['anio'] = anio
                            print("Cambios guardados correctamente")
                            return #luego de guardar sale de la funcion 
                    else:
                        print("El Titulo ingresado no está registrado. ¿Desea Intentar nuevamente?")
                        print("""
                                1-Si.    
                                2-No. """)
                        repetir=int(input("Ingrese un número de opción: "))
                        if repetir == 1:
                            break  # Salir del bucle for y volver a pedir el titulo del libro.
                        elif repetir == 2:
                            return # Salir de la función
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

   
    def editar_autor(self):
        while True:  # Usamos un bucle infinito para repetir la operación hasta que se encuentre un autor válido o se decida salir.
            buscar_autor = input("Ingrese Nombre o Apellido del autor que desea modificar: ")
            if len(self.autores) == 0:
                print("No se encontraron autores registrados.")
                return  # Si no hay autores registrados, salimos de la función.
            else:
                for iterador in self.autores:
                    if iterador['Nombres'] == buscar_autor or iterador['Apellido'] == buscar_autor:
                        print("Nombres:", iterador['Nombres'])
                        print("Apellido:", iterador['Apellido'])
                        
                        print("************************")
                        print("""
                            ¿Qué desea modificar?:
                            1-Nombres.
                            2-Apellido.
                            3-Ambos.
                            4-Salir.
                            """)    
                        opcion = int(input("Ingrese número de opción: "))
                        if opcion == 1:
                            nombreN = input('Ingrese nuevo nombre: ')
                            self.autores[self.autores.index(iterador)]['Nombres'] = nombreN
                            print("Cambios guardados")
                            return
                        elif opcion == 2:
                            Napellido = input('Ingrese nuevo Apellido:')
                            self.autores[self.autores.index(iterador)]['Apellido'] = Napellido
                            print("Cambios guardados")
                            return
                        elif opcion == 3:
                            nombreN = input('Ingrese nuevo nombre: ')
                            self.autores[self.autores.index(iterador)]['Nombres'] = nombreN
                            print("\n")  # Separación "decorativa"
                            Napellido = input('Ingrese nuevo Apellido:')
                            self.autores[self.autores.index(iterador)]['Apellido'] = Napellido
                            print("Cambios guardados")
                            return
                        elif opcion == 4:
                            return  # Salir de la función si se elige esta opción.
                    else:
                        print("El Autor ingresado no está registrado. ¿Desea Intentar nuevamente?")
                        print("""
                                1-Si.    
                                2-No. """)
                        repetir=int(input("Ingrese un número de opción: "))
                        if repetir == 1:
                            break  # Salir del bucle for y volver a pedir el autor.
                        elif repetir == 2:
                            return # Salir de la función 
#-------------------Fin de la clase autores--------------

#--------------inicio de menu-----------------------
class Menu(Biblioteca, Autores):
    def __init__(self):#agregue ésta definición
        
        Biblioteca.__init__(self)
        Autores.__init__(self)
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
                3) Listar autores
                4) Salir
            """)
        fin = False
        while not(fin):
            op = int(input("Ingrese el número de la opción deseada: "))
            if op == 1:
                print("Agregando...")
                self.agregarautor()
                self.menu_autores()
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
