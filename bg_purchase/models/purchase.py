from openerp import fields, models, api
from openerp.tools import amount_to_text_en


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'


    # def _amount_to_text(self, cr, uid, amount, currency_id, context=None):
    #     # Currency complete name is not available in res.currency model
    #     # Exceptions done here (EUR, USD, BRL) cover 75% of cases
    #     # For other currencies, display the currency code
    #     currency = self.pool['res.currency'].browse(cr, uid, currency_id, context=context)
    #     if currency.name.upper() == 'EUR':
    #         currency_name = 'Euro'
    #     elif currency.name.upper() == 'USD':
    #         currency_name = 'Dollars'
    #     elif currency.name.upper() == 'BRL':
    #         currency_name = 'reais'
    #     else:
    #         currency_name = currency.name
    #     #TODO : generic amount_to_text is not ready yet, otherwise language (and country) and currency can be passed
    #     #amount_in_word = amount_to_text(amount, context=context)
    #     return amount_to_text(amount, currency=currency_name)
    #
    # def amount_to_text(self, amount, currency_id):
    #     if not currency_id:
    #         currency_id = self.currency_id.id
    #     res =self._amount_to_text(amount, currency_id)
    #     return res

    # def amount_to_text(self, amount, currency):
    #     cur = currency.name
    #     return amount_to_text_en.amount_to_text(amount, 'en', cur);

    def amount_to_text(self, amount, currency):
        cur = currency.name
        res = self.env['account.invoice'].amount_to_text(amount, cur)
        return res
