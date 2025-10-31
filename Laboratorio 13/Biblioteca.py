class Libro:
    def __init__(self, titulo, autor, genero, paginas, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.paginas = paginas
        self.disponible = disponible

    def prestado(self):
        self.disponible = not self.disponible

    def __str__(self):
        estado = "Disponible ✅" if self.disponible else "Prestado ❌"
        return f"'{self.titulo}' - {self.autor} ({self.genero}, {self.paginas} págs.) - {estado}"


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def añadir_libro(self, libro):
        if libro not in self.libros_prestados:
            self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)

    def __str__(self):
        libros = ", ".join([l.titulo for l in self.libros_prestados]) or "Ninguno"
        return f"{self.nombre} (ID: {self.id_usuario}) - Libros prestados: {libros}"


class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def mostrar_libros(self):
        print("\n📚 Catálogo de libros:")
        if not self.libros:
            print("No hay libros registrados.")
        else:
            for libro in self.libros:
                print(" -", libro)

    def mostrar_usuarios(self):
        print("\n👥 Usuarios registrados:")
        if not self.usuarios:
            print("No hay usuarios registrados.")
        else:
            for usuario in self.usuarios:
                print(" -", usuario)

    def buscar_libro(self, titulo):
        return next((l for l in self.libros if l.titulo.lower() == titulo.lower()), None)

    def buscar_usuario(self, id_usuario):
        return next((u for u in self.usuarios if u.id_usuario == id_usuario), None)

    def prestar_libro(self, titulo, id_usuario):
        libro = self.buscar_libro(titulo)
        usuario = self.buscar_usuario(id_usuario)

        if not libro:
            print("❌ El libro no existe.")
            return
        if not usuario:
            print("❌ Usuario no encontrado.")
            return
        if not libro.disponible:
            print("⚠️ El libro ya está prestado.")
            return

        libro.prestado()
        usuario.añadir_libro(libro)
        print(f"✅ {usuario.nombre} ha tomado prestado '{libro.titulo}'.")

    def devolver_libro(self, titulo, id_usuario):
        libro = self.buscar_libro(titulo)
        usuario = self.buscar_usuario(id_usuario)

        if not libro or not usuario:
            print("❌ Libro o usuario no encontrado.")
            return

        if libro not in usuario.libros_prestados:
            print(f"⚠️ {usuario.nombre} no tenía prestado ese libro.")
            return

        usuario.devolver_libro(libro)
        libro.prestado()
        print(f"📘 {usuario.nombre} ha devuelto '{libro.titulo}'.")

def menu():
    biblioteca = Biblioteca()

    while True:
        print("\n=== 📖 SISTEMA DE GESTIÓN DE BIBLIOTECA ===")
        print("1. Agregar libro")
        print("2. Registrar usuario")
        print("3. Mostrar libros")
        print("4. Mostrar usuarios")
        print("5. Prestar libro")
        print("6. Devolver libro")
        print("7. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            titulo = input("Título del libro: ")
            autor = input("Autor: ")
            genero = input("Género: ")
            paginas = int(input("Número de páginas: "))
            biblioteca.agregar_libro(Libro(titulo, autor, genero, paginas))
            print("✅ Libro agregado correctamente.")

        elif opcion == "2":
            nombre = input("Nombre del usuario: ")
            id_usuario = input("ID del usuario: ")
            biblioteca.registrar_usuario(Usuario(nombre, id_usuario))
            print("✅ Usuario registrado con éxito.")

        elif opcion == "3":
            biblioteca.mostrar_libros()

        elif opcion == "4":
            biblioteca.mostrar_usuarios()

        elif opcion == "5":
            id_usuario = input("Ingrese el ID del usuario: ")
            titulo = input("Ingrese el título del libro a prestar: ")
            biblioteca.prestar_libro(titulo, id_usuario)

        elif opcion == "6":
            id_usuario = input("Ingrese el ID del usuario: ")
            titulo = input("Ingrese el título del libro a devolver: ")
            biblioteca.devolver_libro(titulo, id_usuario)

        elif opcion == "7":
            print("👋 ¡Gracias por usar el sistema de biblioteca!")
            break

        else:
            print("❌ Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
