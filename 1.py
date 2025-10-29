class Pagina:
    def __init__(self, numero, contenido):
        self.numero = numero
        self.contenido = contenido
    def mostrarPagina(self):
        print("Pagina", self.numero, ":", self.contenido)

class Libro:
    def __init__(self, titulo, isbn, paginas):
        self.titulo = titulo
        self.isbn = isbn
        self.paginas = [Pagina(i+1, p) for i, p in enumerate(paginas)]
    def leer(self):
        for p in self.paginas:
            p.mostrarPagina()

class Autor:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
    def mostrarInfo(self):
        print("Autor:", self.nombre, "-", self.nacionalidad)

class Estudiante:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre
    def mostrarInfo(self):
        print("Estudiante:", self.nombre, "-", self.codigo)

class Prestamo:
    def __init__(self, estudiante, libro, fecha_prestamo, fecha_devolucion):
        self.estudiante = estudiante
        self.libro = libro
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
    def mostrarInfo(self):
        print("Prestamo de", self.libro.titulo, "a", self.estudiante.nombre)
        print("Fecha prestamo:", self.fecha_prestamo)
        print("Fecha devolucion:", self.fecha_devolucion)

class Horario:
    def __init__(self, dias, hora_apertura, hora_cierre):
        self.dias = dias
        self.hora_apertura = hora_apertura
        self.hora_cierre = hora_cierre
    def mostrarHorario(self):
        print("Dias:", self.dias, "| Apertura:", self.hora_apertura, "| Cierre:", self.hora_cierre)

class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []
        self.autores = []
        self.prestamos = []
        self.horario = None
    def agregarLibro(self, libro):
        self.libros.append(libro)
    def agregarAutor(self, autor):
        self.autores.append(autor)
    def prestarLibro(self, estudiante, libro, fecha_prestamo, fecha_devolucion):
        prestamo = Prestamo(estudiante, libro, fecha_prestamo, fecha_devolucion)
        self.prestamos.append(prestamo)
        return prestamo
    def asignarHorario(self, horario):
        self.horario = horario
    def mostrarEstado(self):
        print("Biblioteca:", self.nombre)
        if self.horario:
            self.horario.mostrarHorario()
        print("Libros:", [l.titulo for l in self.libros])
        print("Autores:", [a.nombre for a in self.autores])
        print("Prestamos activos:", len(self.prestamos))
    def cerrarBiblioteca(self):
        print("Cerrando biblioteca", self.nombre)
        self.prestamos.clear()

pagina_contenido = ["Inicio", "Contenido", "Fin"]
libro1 = Libro("Python Basico", "12345", pagina_contenido)
autor1 = Autor("Juan Perez", "Boliviano")
horario1 = Horario("Lunes a Viernes", "08:00", "18:00")
est1 = Estudiante("001", "Maria")
biblio = Biblioteca("UMSA")
biblio.asignarHorario(horario1)
biblio.agregarLibro(libro1)
biblio.agregarAutor(autor1)
prestamo1 = biblio.prestarLibro(est1, libro1, "2025-10-28", "2025-11-04")
biblio.mostrarEstado()
prestamo1.mostrarInfo()
biblio.cerrarBiblioteca()
