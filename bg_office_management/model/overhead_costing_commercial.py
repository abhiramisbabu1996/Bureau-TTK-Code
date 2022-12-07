from openerp import models, fields, api, _


class OverheadCategory(models.Model):
    _name = 'overhead.category'

    name = fields.Char('Category Name')


class OverheadSubCategory(models.Model):
    _name = 'overhead.subcategory'

    name = fields.Char('Sub Category Name')


class OverheadCostingCommercial(models.Model):
    _name = 'overheadcost.commercial'
    _rec_name = 'overhead_category'


    overhead_category = fields.Many2one('overhead.category', 'Overhead Category')
    overhead_sub_category = fields.Many2one('overhead.subcategory', 'Overhead Sub Category')
    estimated_total_amount = fields.Float('Estimated Sub Category')
    month_select = fields.Selection(
        [('january', 'January'), ('february', 'February'), ('march', 'March'), ('april', 'April'), ('may', 'May'),
         ('june', 'June'), ('july', 'July'), ('august', 'August'), ('september', 'September'), ('october', 'October'),
         ('november', 'November'), ('december', 'December')],string="Month")
    actual_value = fields.Float()
