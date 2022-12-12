from openerp import models, fields, api, _
from openerp import tools, _
from datetime import datetime, date, timedelta


class OverheadProjectReport(models.TransientModel):
    _name = 'overhead.project'

    project_id = fields.Many2one('project.project', 'Project Name')
    month_select = fields.Selection(
        [('january', 'January'), ('february', 'February'), ('march', 'March'), ('april', 'April'), ('may', 'May'),
         ('june', 'June'), ('july', 'July'), ('august', 'August'), ('september', 'September'), ('october', 'October'),
         ('november', 'November'), ('december', 'December')], string="Month")

    @api.multi
    def action_overhead_project(self):
        datas = {
            'ids': self._ids,
            'model': self._name,
            'form': self.read(),
            'context': self._context,
        }

        return {
            'name': 'Project Overhead Distribution Report',
            'type': 'ir.actions.report.xml',
            'report_name': 'bg_office_management.report_overhead_project_template',
            'datas': datas,
            'report_type': 'qweb-pdf'
        }

    @api.multi
    def action_overhead_project_view(self):
        datas = {
            'ids': self._ids,
            'model': self._name,
            'form': self.read(),
            'context': self._context,
        }
        return {
            'name': 'Project Overhead Distribution Report',
            'type': 'ir.actions.report.xml',
            'report_name': 'bg_office_management.report_overhead_project_template',
            'datas': datas,
            'report_type': 'qweb-html',
        }

    @api.multi
    def get_details(self):
        lst = []
        lst_dict = []
        domain = []
        if self.project_id:
            domain += [('project_id', '=', self.project_id.id)]
        if self.month_select:
            domain += [('month_select', '=', self.month_select)]
        records = self.env['projectoverhead.distribution'].search(domain)
        for rec in records:
            jan, feb, mar, apr, may, june, july, aug, sep, oct, nov, dec = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
            vals_sample = {
                'project_id': rec.project_id.id,
            }
            if vals_sample not in lst_dict:
                # print("you there??")
                if rec.month_select == 'january':
                    jan = rec.actual_value
                if rec.month_select == 'february':
                    feb = rec.actual_value
                if rec.month_select == 'march':
                    mar = rec.actual_value
                if rec.month_select == 'april':
                    apr = rec.actual_value
                if rec.month_select == 'may':
                    may = rec.actual_value
                if rec.month_select == 'june':
                    june = rec.actual_value
                if rec.month_select == 'july':
                    july = rec.actual_value
                if rec.month_select == 'august':
                    aug = rec.actual_value
                if rec.month_select == 'september':
                    sep = rec.actual_value
                if rec.month_select == 'october':
                    oct = rec.actual_value
                if rec.month_select == 'november':
                    nov = rec.actual_value
                if rec.month_select == 'december':
                    dec = rec.actual_value

                vals = {
                    'pid': rec.project_id.id,
                    'project_id': rec.project_id.name,
                    'project_value': rec.project_value,
                    'row_percentage': 0,
                    'jan': jan,
                    'feb': feb,
                    'mar': mar,
                    'apr': apr,
                    'may': may,
                    'june': june,
                    'july': july,
                    'aug': aug,
                    'sep': sep,
                    'oct': oct,
                    'nov': nov,
                    'dec': dec,
                    'total': 0,
                    'e_total_project_val': 0,
                    'per_total': 0,
                    'jan_total': 0,
                    'feb_total': 0,
                    'mar_total': 0,
                    'may_total': 0,
                    'june_total': 0,
                    'july_total': 0,
                    'aug_total': 0,
                    'sep_total': 0,
                    'oct_total': 0,
                    'nov_total': 0,
                    'dec_total': 0,
                    'grand_total': 0,

                }
                lst.append(vals)
                lst_dict.append(vals_sample)
            else:
                for dict in lst:
                    if dict['pid'] == rec.project_id.id:
                        if rec.month_select == 'january':
                            dict['jan'] = rec.actual_value
                        if rec.month_select == 'february':
                            dict['feb'] = rec.actual_value
                        if rec.month_select == 'march':
                            dict['mar'] = rec.actual_value
                        if rec.month_select == 'april':
                            dict['apr'] = rec.actual_value
                        if rec.month_select == 'may':
                            dict['may'] = rec.actual_value
                        if rec.month_select == 'june':
                            dict['june'] = rec.actual_value
                        if rec.month_select == 'july':
                            dict['july'] = rec.actual_value
                        if rec.month_select == 'august':
                            dict['aug'] = rec.actual_value
                        if rec.month_select == 'september':
                            dict['sep'] = rec.actual_value
                        if rec.month_select == 'october':
                            dict['oct'] = rec.actual_value
                        if rec.month_select == 'november':
                            dict['nov'] = rec.actual_value
                        if rec.month_select == 'december':
                            dict['dec'] = rec.actual_value
                        dict['total'] = jan + feb + mar + apr + may + june + july + aug + sep + oct + nov + dec
        sum1, row_percentage, jan_total, feb_total, mar_total, apr_total, may_total, june_total, july_total, aug_total, sep_total, oct_total, nove_total, dec_total, grand_total = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        for dict in lst:
            dict['total'] = dict['jan'] + dict['feb'] + dict['mar'] + dict['apr'] + dict['may'] + dict['june'] + dict[
                'july'] + dict['aug'] + dict['sep'] + dict['oct'] + dict['nov'] + dict['dec']
            sum1 = sum1 + dict['project_value']
            dict['row_percentage'] = round(((dict['total']/dict['project_value'])*100),2)
            # sum2 = sum2 + dict['e_amount_month']
            jan_total = jan_total + dict['jan']
            feb_total = feb_total + dict['feb']
            mar_total = mar_total + dict['mar']
            apr_total = apr_total + dict['apr']
            may_total = may_total + dict['may']
            june_total = june_total + dict['june']
            july_total = july_total + dict['july']
            aug_total = aug_total + dict['aug']
            sep_total = sep_total + dict['sep']
            oct_total = oct_total + dict['oct']
            nove_total = nove_total + dict['nov']
            dec_total = dec_total + dict['dec']
            grand_total = grand_total + dict['total']

        for dict in lst:
            dict['e_totalproject_value'] = sum1
            dict['jan_total'] = jan_total
            dict['feb_total'] = feb_total
            dict['mar_total'] = mar_total
            dict['apr_total'] = apr_total
            dict['may_total'] = may_total
            dict['june_total'] = june_total
            dict['july_total'] = july_total
            dict['aug_total'] = aug_total
            dict['sep_total'] = sep_total
            dict['oct_total'] = oct_total
            dict['nove_total'] = nove_total
            dict['dec_total'] = dec_total
            dict['grand_total'] = grand_total
            dict['per_total'] = round((dict['grand_total']/dict['e_totalproject_value'])*100,2)
            # print("wewrtewrew", dict['e_amount_month_total'])
            # print("qqqqqqqqqqqqqqq", dict['grand_total'])
        return lst
