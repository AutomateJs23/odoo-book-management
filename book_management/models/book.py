from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class Book(models.Model):
    _name = "book.book"
    _description = "Book"

    name = fields.Char(
        string="Book Title",
        required=True,
    )
    book_image = fields.Image(
        string="Book Image"
    )
    author_ids = fields.Many2many(
        "book.author",
        "book_author_rel",
        "author_id",
        "book_id",
        string="Author",
        required=True,
    )
    isbn = fields.Char(
        string="International Standard Book Number",
        required=True,
    )
    category_ids = fields.Many2many(
        "book.category",
        "categ_id",
        "book_id",
        string="Categories",
        required=True,
    )
    book_total = fields.Integer(
        string="Book Total",
    )
    book_available = fields.Integer(
        string="Book Available",
        compute="_compute_book_available",
    )
    description = fields.Text(
        string="Description",
    )

    @api.onchange("isbn")
    def _onchange_check_isbn(self):
        for obj in self:
            try:
                obj.isbn = int(obj.isbn)
            except:
                raise ValidationError(
                    _(
                        "(International Standard Book Number) must be number!"
                    )
                )

    @api.depends("book_total")
    def _compute_book_available(self):
        for obj in self:
            obj.book_available = obj.book_total
