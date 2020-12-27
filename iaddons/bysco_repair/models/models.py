# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Repair(models.Model):
    _name = 'repair.order'
    _description = 'Inheritance'
    _inherit = 'repair.order'

    def print_repair_order(self):
        return self.env.ref('action_bysco_repair').report_action(self)