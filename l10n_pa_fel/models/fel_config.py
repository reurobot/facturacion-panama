# -*- coding: utf-8 -*-

from odoo import models, fields

class FelConfig(models.Model):
    _name = 'fel.config'
    _description = 'FEL Configuration'

    name = fields.Char(string='Name', required=True)
    token_empresa = fields.Char(string='Token Empresa', required=True)
    token_password = fields.Char(string='Token Password', required=True)
    wsdl_url = fields.Char(string='WSDL URL', default='https://demoemision.thefactoryhka.com.pa/ws/obj/v1.0/Service.svc?singleWsdl', required=True)
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company)