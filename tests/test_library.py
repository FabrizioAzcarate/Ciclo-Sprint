import unittest
from services.library_service import LibraryService

class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.library = LibraryService()
        self.library.add_game("Zelda", "Aventura")

    def test_add_game(self):
        self.library.add_game("Mario", "Plataforma")
        self.assertEqual(len(self.library.games), 2)

    def test_borrow_game(self):
        self.library.borrow_game("Zelda")
        game = self.library.find_game("Zelda")
        self.assertTrue(game.is_borrowed)

    def test_return_game(self):
        self.library.borrow_game("Zelda")
        self.library.return_game("Zelda")
        game = self.library.find_game("Zelda")
        self.assertFalse(game.is_borrowed)

if __name__ == "__main__":
    unittest.main()