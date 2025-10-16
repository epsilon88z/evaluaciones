class Libro:
    def __init__(self, id=None, titulo="", autor="", anio=0, categoria=""):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.categoria = categoria
        
    def __str__(self):
        return f'[{self.id}] {self.titulo} - {self.autor} ({self.anio} -> -> {self.categoria})'