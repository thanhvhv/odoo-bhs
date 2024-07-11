# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from itertools import count

class CreateUserEmployee(models.Model):
    _inherit = "hr.employee"

    @api.model_create_multi
    def create(self, vals):
        recs = super(CreateUserEmployee, self).create(vals) #tạo ra 1 nvien
        for rec in recs:
            if rec.env['res.users'].sudo().search([('login', '=', rec.work_email)]).id:
                raise ValidationError(_('This email is already used by another user'))
            elif not rec.user_id:
                # user_partner_id = rec.env['res.partner'].sudo().search([('email', '=', rec.work_email), ('is_company', '=', False)]).id
                user_info = {'name': rec.name,
                             'login': rec.work_email,
                             'email': rec.work_email,
                             'state': 'active',
                             'partner_id': rec.work_contact_id.id}
                account = self.env['res.users'].sudo().create(user_info)
                rec.user_id = account.id
        return recs


class HrApplicantInherit(models.Model):
    _inherit = 'hr.applicant'

    # work_email = fields.Char(string='Work email')

    def create_employee_from_applicant(self):
        res = super(HrApplicantInherit, self).create_employee_from_applicant()
        res['context']['default_work_email'] = None
        res['context']['default_work_contact_id'] = self.partner_id.id

        return res
