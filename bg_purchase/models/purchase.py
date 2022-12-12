from openerp import fields, models, api
from openerp.tools import amount_to_text_en


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    supplier_quotation_reference = fields.Char()

    @api.model
    def create(self, vals):
        if vals.get('name'):
            sequence = vals.get('name').split('/')
        return super(PurchaseOrder,self).create(vals)


    def amount_to_text(self, amount, currency):
        cur = currency.name
        res = self.env['account.invoice'].amount_to_text(amount, cur)
        return res
