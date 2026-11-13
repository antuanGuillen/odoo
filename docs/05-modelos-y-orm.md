# 5. Modelos y ORM

El ORM permite trabajar con registros usando modelos Python en lugar de escribir SQL para cada operación.

Ejemplo conceptual:

```python
from odoo import models, fields

class Libro(models.Model):
    _name = "sge.libro"
    _description = "Libro"

    name = fields.Char(string="Título", required=True)
    paginas = fields.Integer(string="Páginas", default=1)
    disponible = fields.Boolean(default=True)
```

## Operaciones habituales
```python
Libro = self.env["sge.libro"]

# Crear
registro = Libro.create({"name": "Python práctico", "paginas": 240})

# Buscar
libros = Libro.search([("disponible", "=", True)])

# Leer
titulo = registro.name

# Escribir
registro.write({"disponible": False})

# Eliminar (solo en datos de prueba)
registro.unlink()
```

## Dominios
Un dominio filtra registros. Ejemplo: `[("paginas", ">", 100)]`.

## Reto
Añade un campo `isbn` y evita duplicados mediante una restricción SQL o una validación Python apropiada. Investiga las diferencias y cuándo conviene cada enfoque.
