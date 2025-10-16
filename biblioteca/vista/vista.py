class Vista:
    def menu(self):
        print("============ 📚 MENU 📚 ============")
        print("1 -> Agregar  Libro")
        print("2 -> Mostrar  Libros")
        print("3 -> Editar   Libro")
        print("4 -> Eliminar Libro")
        print("5 -> Salir ")
        print("="*36)
        return input('Seleccione una opción: ')
    
    def libro_form(self):
        titulo = input('Titulo: ')
        autor = input('Autor: ')
        anio = int(input('Año: '))
        categoria = input('Categoria: ')
        return {'titulo':titulo, 'autor': autor, 'anio':anio, 'categoria':categoria}
    
    def mostrar_libros(self, libros):
        if not libros:
            ('no hay libros registrados')
        else:
            for l in libros:
                print(l)
                
    def pedir_id(self, accion=""):
        try:
            return int(input(f'Ingrese el id a {accion}: '))
        except ValueError:
            print("id invalido")
    
    def mensaje(self,texto):
        print(texto)
    
    
        
        
        
