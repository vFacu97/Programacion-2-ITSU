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

    def mostrar_libro(self):
        if len in (self.libros) == 0:
            print("No se encontraron libros en la biblioteca.")
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


libros = Libros()
libros.agregar_libro()
libros.mostrar_libro()
libros.editar_libro()
libros.mostrar_libro()
#comentario de prueba