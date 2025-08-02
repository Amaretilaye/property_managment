from odoo import  fields, models, api


class Lease(models.Model):
    _name = 'lease.management'
    _description = 'Lease Management'


    name = fields.Char(string='Lease Name', store=True)
    tenant_id = fields.Many2one('tenant.management', string='Tenant', required=True)
    property_id = fields.Many2one('property.management', string='Property', required=True)
    start_date = fields.Date(string='Start Date', required=True)
    end_date = fields.Date(string='End Date', required=True)
    monthly_rent = fields.Float(string='Monthly Rent', required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('active', 'Active'),
        ('expired', 'Expired')
    ], string='Status', default='draft')
