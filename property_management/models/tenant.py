from odoo import models, fields, api


class Tenant(models.Model):
    _name = 'tenant.management'
    _description = 'Tenant Management'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    id_number = fields.Char(string='ID Number')
    lease_ids = fields.One2many('lease.management', 'tenant_id', string='Leases')  # one tenant can have multiple leases
