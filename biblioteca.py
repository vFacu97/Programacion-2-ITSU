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
                    opcion = int(input("¿Que opción desea modificar?: 1 Nombre - 2 Autor - 3 Año de Edición"))
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


#---------------comienzo de clase de autores----------------
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
#-------------------Fin de la clase autores--------------