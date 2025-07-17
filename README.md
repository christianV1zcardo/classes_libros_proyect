# Gestor de Libros de Biblioteca

Este es un mini proyecto de Python que implementa un sistema básico para gestionar libros en una biblioteca utilizando los principios de la Programación Orientada a Objetos (POO).

---

## 📚 Descripción del Proyecto

El objetivo de este proyecto es consolidar los conceptos de clases, objetos y la gestión de su estado. Se enfoca en la creación de dos clases principales: `Libro` para representar las propiedades y el estado de un libro individual, y `Biblioteca` para gestionar una colección de libros y sus operaciones básicas.

---

## ✨ Características Principales

### Clase `Libro`
Representa un libro individual con las siguientes características:
* **Atributos:** `id`, `titulo`, `autor`, `ISBN`, `disponible` (estado booleano).
* **Validación Básica:** El constructor (`__init__`) incluye validaciones de tipo para sus atributos.
* **Métodos de Estado:** `marcarse_como_prestado()` y `marcarse_como_devuelto()` para cambiar la disponibilidad del libro.
* **Representación (`__repr__`)**: Proporciona una representación legible del objeto.

### Clase `Biblioteca`
Actúa como el gestor de la colección de libros:
* **Atributos de Clase:** `_libros_disponibles`, `_libros_no_disponibles`, `_todos_los_libros` (listas que contienen objetos `Libro`).
* **Método de Clase `añadir_libro()` (`@classmethod`):** Crea una nueva instancia de `Libro` y la añade a las colecciones de la biblioteca. Genera un `id` simple automáticamente.
* **Métodos de Clase para Gestión (`@classmethod`):**
    * `prestar_libro()`: Marca un libro como prestado y lo mueve entre las listas de disponibilidad.
    * `devolver_libro()`: Marca un libro como devuelto y lo mueve entre las listas de disponibilidad.
* **Métodos de Clase para Listado (`@classmethod`):**
    * `listar_libros_disponibles()`: Muestra los títulos de los libros actualmente disponibles.
    * `listar_todos_los_libros()`: Muestra los títulos de todos los libros en la biblioteca.

---

## 🧑‍💻 Autor

[Christian Vizcardo]
[www.linkedin.com/in/christian-vizcardo]