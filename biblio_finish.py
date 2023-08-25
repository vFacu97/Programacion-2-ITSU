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
