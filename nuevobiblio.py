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
        for autor in self.autores:
            if autor['Nombres'] == nombre_buscar:
                return autor
        return None
    
    def editar_autor(self, autor_encontrado):
        nuevo_nombre = input("Nuevo nombre: ")
        nuevo_apellido = input("Nuevo apellido: ")
        autor_encontrado['Nombres'] = nuevo_nombre
        autor_encontrado['Apellido'] = nuevo_apellido
        print("Autor modificado.")
    
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
        nombre_buscar = input("Ingrese el nombre del autor a buscar y editar: ")
        autor_encontrado = autor.buscar_autor(nombre_buscar)
        if autor_encontrado:
            autor.editar_autor(autor_encontrado)
        else:
            print("Autor no encontrado.")
    elif opcion == 4:
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
