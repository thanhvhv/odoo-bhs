# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from datetime import date
from dateutil.relativedelta import relativedelta
from odoo import api, fields, models

class Lead(models.Model):
    _inherit = 'crm.lead'

    hide = fields.Boolean(string='Hide this Opportunity')

    def action_hide(self):
        for rec in self:
            rec.hide = True
        return {'type': 'ir.actions.client', 'tag': 'reload'}

    def action_unhide(self):
        for rec in self:
            rec.hide = False
        return {'type': 'ir.actions.client', 'tag': 'reload'}
