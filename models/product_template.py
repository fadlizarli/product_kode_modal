from odoo import fields, models

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    kode_modal = fields.Char(string='Kode Modal')

    def action_open_kode_modal_wizard(self):
        wizard = self.env['kode.modal.wizard'].create({
            'product_tmpl_id': self.id,
            'harga_modal': self.standard_price,
        })
        return {
            'type': 'ir.actions.act_window',
            'name': 'Generator Kode Modal',
            'res_model': 'kode.modal.wizard',
            'res_id': wizard.id,
            'view_mode': 'form',
            'target': 'new',
        }

class ProductProduct(models.Model):
    _inherit = 'product.product'

    kode_modal = fields.Char(
        string='Kode Modal',
        related='product_tmpl_id.kode_modal',
        store=True
    )
