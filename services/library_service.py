from models.game import Game

class LibraryService:
    def __init__(self):
        self.games = []

    def add_game(self, title, genre):
        if self.find_game(title):
            raise Exception(f"El juego '{title}' ya existe en la biblioteca")

        game = Game(title, genre)
        self.games.append(game)
        return game

    def list_games(self):
        return self.games

    def find_game(self, title):
        for game in self.games:
            if game.title.lower() == title.lower():
                return game
        return None

    def borrow_game(self, title):
        game = self.find_game(title)
        if not game:
            raise Exception("Juego no encontrado")
        game.borrow()

    def return_game(self, title):
        game = self.find_game(title)
        if not game:
            raise Exception("Juego no encontrado")
        game.return_game()
