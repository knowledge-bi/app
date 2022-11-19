# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


class AccountPayment(models.Model):
    _inherit = 'account.payment'

    destination_account_id = fields.Many2one(domain="[('company_id', '=', company_id)]")

    @api.model
    def create(self, vals):
        new_record = super(AccountPayment, self.with_context(skip_account_move_synchronization=True)).create(vals)
        return new_record
