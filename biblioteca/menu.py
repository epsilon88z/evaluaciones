from vista.vista import Vista
from modelo.libro import Libro
from controlador.controlador import ControladorLibro

def inicio():
    vista = Vista()
    ctrl = ControladorLibro()
    while True:
        opcion = vista.menu()
        if opcion == "1":
            print("Agregar Libro")
            datos = vista.libro_form() #pedir los datos al usuario
            libro = Libro(None, datos['titulo'], datos['autor'], datos['anio'], datos['categoria'])
            libro = ctrl.agregar_libro(libro)
            vista.mensaje(f'Libro agregado con ID: [{libro.id}]')
        elif opcion == "2":
            print("Lista Libros")
            libros = ctrl.listar_libros()
            vista.mostrar_libros(libros)
        elif opcion == "3":
            print("Editar Libro")
            libros = ctrl.listar_libros()
            vista.mostrar_libros(libros)
            id_libro = vista.pedir_id("modificar")
            if id_libro:
                datos = vista.libro_form()
                libro = Libro(id_libro, datos['titulo'], datos['autor'], datos['anio'], datos['categoria'])
                actualizado = ctrl.modificar_libro(libro)
                vista.mensaje("libro acatulizado" if actualizado else "id no encontrado")
                
        elif opcion == "4":
            print("Eliminar Libro")
            libros = ctrl.listar_libros()
            vista.mostrar_libros(libros)
            id_libro = vista.pedir_id("Eliminar")
            if id_libro:
                eliminado = ctrl.eliminar_libro(id_libro)
                vista.mensaje("libro eliminado!" if eliminado else "id no encontrado")
                
        elif opcion == "5":
            print("¡Hasta Luego!")
            break
        else:
            print(f'opción: {opcion} seleccionada aun en desarrollo')

inicio()