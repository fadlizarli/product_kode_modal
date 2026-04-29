from odoo import fields, models

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    kode_modal = fields.Char(string='Kode Modal')

class ProductProduct(models.Model):
    _inherit = 'product.product'

    kode_modal = fields.Char(
        string='Kode Modal',
        related='product_tmpl_id.kode_modal',
        store=True
    )
