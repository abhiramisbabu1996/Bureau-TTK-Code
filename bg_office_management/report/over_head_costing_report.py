from openerp import models, fields, api, _
from openerp import tools, _
from datetime import datetime, date, timedelta


class OverheadCostingReport(models.TransientModel):
    _name = 'overhead.costing.reports'

    overhead_category = fields.Many2one('overhead.category', 'Category')
    overhead_sub_category = fields.Many2one('overhead.subcategory', 'Sub Category')
    month_select = fields.Selection(
        [('january', 'January'), ('february', 'February'), ('march', 'March'), ('april', 'April'), ('may', 'May'),
         ('june', 'June'), ('july', 'July'), ('august', 'August'), ('september', 'September'), ('october', 'October'),
         ('november', 'November'), ('december', 'December')], string="Month")

    @api.multi
    def action_overhead_costing(self):
        datas = {
            'ids': self._ids,
            'model': self._name,
            'form': self.read(),
            'context': self._context,
        }

        return {
            'name': 'Overhead Costing By Commercial Report',
            'type': 'ir.actions.report.xml',
            'report_name': 'bg_office_management.report_overhead_costing_template',
            'datas': datas,
            'report_type': 'qweb-pdf'
        }

    @api.multi
    def action_overhead_costing_view(self):
        datas = {
            'ids': self._ids,
            'model': self._name,
            'form': self.read(),
            'context': self._context,
        }
        return {
            'name': 'Overhead Costing By Commercial Report',
            'type': 'ir.actions.report.xml',
            'report_name': 'bg_office_management.report_overhead_costing_template',
            'datas': datas,
            'report_type': 'qweb-html',
        }

    @api.multi
    def get_details(self):
        lst = []
        domain = []
        if self.overhead_category:
            domain += [('overhead_category', '=', self.overhead_category.id)]
        if self.overhead_sub_category:
            domain += [('overhead_sub_category', '=', self.overhead_category.id)]
        if self.month_select:
            domain += [('month_select', '=', self.month_select)]
        records = self.env['overheadcost.commercial'].search(domain)
        for rec in records:
            vals = {
                'overhead_category': rec.overhead_category.name,
                'overhead_sub_category': rec.overhead_sub_category.name,
                'month_select': rec.month_select,
                'actual_value': rec.actual_value,
                'total_amount': 0,
            }
            lst.append(vals)
        return lst










