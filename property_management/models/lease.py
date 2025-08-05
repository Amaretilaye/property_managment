from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import timedelta


class Lease(models.Model):
    _name = 'lease.management'
    _description = 'Lease'

    name = fields.Char(string='Lease Name', compute='_compute_lease_name', store=True)
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
    payment_ids = fields.One2many('rent.payment', 'lease_id', string='Payments')

    @api.depends('tenant_id', 'property_id')
    def _compute_lease_name(self):
        for lease in self:
            lease.name = f"Lease {lease.tenant_id.name} - {lease.property_id.name}"

    def action_active(self):
        self.state = 'active'
        self.property_id.status = 'rented'

    def action_expired(self):
        self.state = 'expired'
        self.property_id.status = 'available'

    @api.onchange('property_id')
    def _onchange_property(self):
        if self.property_id:
            self.monthly_rent = self.property_id.price_per_month



