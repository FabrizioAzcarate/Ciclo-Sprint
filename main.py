from services.library_service import LibraryService

def main():
    library = LibraryService()

    library.add_game("FIFA 24", "Deportes")
    library.add_game("The Witcher 3", "RPG")

    print("Lista de juegos:")
    for game in library.list_games():
        print(game)

    print("\nPrestando juego...")
    library.borrow_game("FIFA 24")

    for game in library.list_games():
        print(game)

if __name__ == "__main__":
    main()