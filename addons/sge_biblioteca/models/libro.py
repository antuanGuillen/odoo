from odoo import fields, models


class SgeLibro(models.Model):
    _name = "sge.libro"
    _description = "Libro de biblioteca"
    _order = "name"

    name = fields.Char(string="Título", required=True)
    autor = fields.Char(string="Autor")
    isbn = fields.Char(string="ISBN", copy=False)
    paginas = fields.Integer(string="Número de páginas", default=1)
    fecha_publicacion = fields.Date(string="Fecha de publicación")
    disponible = fields.Boolean(string="Disponible", default=True)
    notas = fields.Text(string="Notas")

    _sql_constraints = [
        (
            "isbn_unico",
            "unique(isbn)",
            "El ISBN debe ser único.",
        ),
    ]
