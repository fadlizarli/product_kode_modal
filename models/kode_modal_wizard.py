from odoo import api, fields, models

KODE_PERTAMA = {'1': 'M', '2': 'O', '3': 'B', '4': 'I', '5': 'L',
                '6': 'S', '7': 'E', '8': 'D', '9': 'A', '0': 'N'}
KODE_KEDUA   = {'1': 'A', '2': 'B', '3': 'C', '4': 'D', '5': 'E',
                '6': 'F', '7': 'G', '8': 'H', '9': 'I', '0': 'L'}


def _encode(price, mapping):
    """Encode an integer price into modal code letters + unit suffix."""
    price = int(round(price))
    if price <= 0:
        return ''
    if price % 1_000_000 == 0:
        number, suffix = price // 1_000_000, 'JT'
    elif price % 1_000 == 0:
        number, suffix = price // 1_000, 'RB'
    elif price % 100 == 0:
        number, suffix = price // 100, 'RT'
    else:
        number, suffix = price, ''
    letters = ''.join(mapping.get(d, d) for d in str(number))
    return f"{letters} {suffix}" if suffix else letters


class KodeModalWizard(models.TransientModel):
    _name = 'kode.modal.wizard'
    _description = 'Generator Kode Modal'

    product_tmpl_id = fields.Many2one('product.template', required=True, ondelete='cascade')

    harga_modal = fields.Float(string='Harga Modal (Rp)', digits=(16, 0))

    cipher = fields.Selection(
        [('1', 'Kode 1 – MOBILS EDAN'), ('2', 'Kode 2 – ABCDEFGHIL')],
        string='Jenis Kode',
        default='1',
        required=True,
    )

    hasil_kode1 = fields.Char(string='Hasil Kode 1', compute='_compute_hasil', store=False)
    hasil_kode2 = fields.Char(string='Hasil Kode 2', compute='_compute_hasil', store=False)

    @api.depends('harga_modal')
    def _compute_hasil(self):
        for rec in self:
            rec.hasil_kode1 = _encode(rec.harga_modal, KODE_PERTAMA)
            rec.hasil_kode2 = _encode(rec.harga_modal, KODE_KEDUA)

    def action_terapkan(self):
        kode = self.hasil_kode1 if self.cipher == '1' else self.hasil_kode2
        self.product_tmpl_id.kode_modal = kode
        return {'type': 'ir.actions.act_window_close'}
