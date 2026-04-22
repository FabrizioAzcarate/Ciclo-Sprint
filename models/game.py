class Game:
    def __init__(self, title, genre):
        self.title = title
        self.genre = genre
        self.is_borrowed = False

    def borrow(self):
        if self.is_borrowed:
            raise Exception(f"El juego '{self.title}' ya está prestado")
        self.is_borrowed = True

    def return_game(self):
        if not self.is_borrowed:
            raise Exception(f"El juego '{self.title}' no estaba prestado")
        self.is_borrowed = False

    def __str__(self):
        status = "Prestado" if self.is_borrowed else "Disponible"
        return f"{self.title} - {self.genre} ({status})"