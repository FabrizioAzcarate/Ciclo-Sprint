# Biblioteca de Videojuegos

## Descripción del proyecto
Este proyecto consiste en el desarrollo de una aplicación en Python que permite gestionar una biblioteca personal de videojuegos.

El sistema permite registrar juegos, listarlos y administrar su estado (disponible o prestado).

---

## Funcionalidades implementadas

- Agregar videojuegos  
- Listar videojuegos  
- Buscar un videojuego por nombre  
- Prestar un videojuego  
- Devolver un videojuego  
- Validación de errores:
  - Evita duplicados  
  - Controla juegos inexistentes  
  - Evita prestar juegos ya prestados  

---

## Estructura del proyecto

El proyecto se organiza en:

- `models/`: contiene la clase `Game`  
- `services/`: contiene la lógica (`LibraryService`)  
- `main.py`: punto de ejecución y pruebas  

---

## Ejecución

```bash
python main.py
