from services.library_service import LibraryService

def main():
    library = LibraryService()

    # Agregar juegos
    try:
        library.add_game("FIFA 24", "Deportes")
        library.add_game("The Witcher 3", "RPG")
        library.add_game("FIFA 24", "Deportes")  # Prueba duplicado
    except Exception as e:
        print(f"Error: {e}")

    # Listar juegos
    print("\n📋 Lista de juegos:")
    for game in library.list_games():
        print(game)

    # Prestar juego
    print("\n🎮 Prestando juego...")
    try:
        library.borrow_game("FIFA 24")
    except Exception as e:
        print(f"Error: {e}")

    for game in library.list_games():
        print(game)

    # Devolver juego
    print("\n🔄 Devolviendo juego...")
    try:
        library.return_game("FIFA 24")
    except Exception as e:
        print(f"Error: {e}")

    for game in library.list_games():
        print(game)


if __name__ == "__main__":
    main()
