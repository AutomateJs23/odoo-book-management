from odoo import fields, models


class BookCategory(models.Model):
    _name = "book.category"
    _description = "Book Category"

    name = fields.Char(
        string="Category Name",
        required=True,
    )
    description = fields.Text(
        string="Description",
    )
