class Libro:
    
    def __init__(self, id, titulo, autor, ISBN, disponible=True):
        
        # Manejo de errores para id que debe ser int
        if not isinstance(id, int):
            raise TypeError("id debe ser un int")
        
        # Manejo de errores para los valores que deben ser str
        for data in [titulo, autor, ISBN]:
            if not isinstance(data, str):
                raise TypeError(f"{data} debe ser un str")
        
        # Manejo de errores para disponible que debe ser un booleano
        if not isinstance(disponible, bool):
            raise TypeError("disponible debe ser un bool")
        
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.ISBN = ISBN
        self.disponible = disponible
        
        
    def __repr__(self):
        return (f"Libro(ID={self.id}, "
                f"titulo={self.titulo}, "
                f"autor={self.autor}, "
                f"ISBN={self.ISBN}, "
                f"disponible={self.disponible})")
    
        
    def marcarse_como_prestado(self):
        self.disponible = False
        
        
    def marcarse_como_devuelto(self):
        self.disponible = True
        
        
class Biblioteca:
    
    _libros_disponibles = []
    _libros_no_disponibles = []
    _todos_los_libros = []
    
    
    def __init__(self):
        print("Biblioteca creada")
    
    
    @classmethod
    def añadir_libro(cls, titulo, autor, ISBN):
        
        if cls._todos_los_libros:
            id = len(cls._todos_los_libros) + 1
            
        else:
            id = 1
            
        libro = Libro(id, titulo, autor, ISBN)
        cls._libros_disponibles.append(libro)
        cls._todos_los_libros.append(libro)
        
        print(f"Libro '{titulo}' añadido correctamente a la biblioteca!")
    
    
    @classmethod
    def prestar_libro(cls, titulo, nombre='Cliente'):
        # Si el libro está disponible lo prestamos y cambiamos de lista
        for libro in cls._libros_disponibles:
            if titulo == libro.titulo:
                libro.marcarse_como_prestado()
                cls._libros_disponibles.remove(libro)
                cls._libros_no_disponibles.append(libro)
                print(f"El libro '{titulo}' fue prestado a {nombre}")
                return
            
        print(f"El libro '{titulo}' no se encuentra disponible.")
    
    
    @classmethod
    def devolver_libro(cls, titulo, nombre='Cliente'):
        # Si el libro no está disponible lo recibimos
        for libro in cls._libros_no_disponibles:
            if titulo == libro.titulo:
                libro.marcarse_como_devuelto()
                cls._libros_no_disponibles.remove(libro)
                cls._libros_disponibles.append(libro)
                print(f"El libro '{titulo}' fue devuelto por {nombre}")
                return
        
        print(f"El libro '{titulo}' no nos pertenece.")
        
        
    @classmethod
    def listar_libros_disponibles(cls):
        
        print(f"Estos son los {len(cls._libros_disponibles)} libros que " 
              "tenemos disponibles:\n")
        
        for libro in cls._libros_disponibles:
            print(f"- {libro.titulo}")
            
    
    @classmethod
    def listar_todos_los_libros(cls):
        
        print(f"\nEstos son {len(cls._todos_los_libros)} los libros que "
              "nos pertenecen, entre prestados y disponibles")
        
        for libro in cls._todos_los_libros:
            print(f"- {libro.titulo}")