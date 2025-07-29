from odoo import models, fields, api


class Property(models.Model):
    _name = 'property.management'
    _description = 'Property'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Property Name', required=True)
    property_type = fields.Selection([
        ('apartment', 'Apartment'),
        ('villa', 'Villa'),
        ('office', 'Office'),
        ('commercial', 'Commercial')
    ], string='Type', default='apartment', required=True)
    company_id = fields.Many2one('res.company', store=True, copy=False,
                                 string="Company",
                                 default=lambda self: self.env.user.company_id.id)
    price_per_month = fields.Float(string='Price per Month', required=True)
    currency_id = fields.Many2one('res.currency', string="Currency",
                                  related='company_id.currency_id',
                                  default=lambda self: self.env.user.company_id.currency_id.id)
    status = fields.Selection([
        ('available', 'Available'),
        ('rented', 'Rented'),
        ('maintenance', 'Maintenance')
    ], string='Status', default='available', required=True)
    image = fields.Binary(string='Image')
    description = fields.Text(string='Description')
    feature_ids = fields.Many2many('property.feature', string='Features')



    num_bedrooms = fields.Integer(string="Bedrooms", help="Only for Apartments/Villas")
    num_floors = fields.Integer(string="Floors", help="Mainly for Villas/Commercial")
    has_parking = fields.Boolean(string="Parking", help="Common for Offices/Commercial")
    license_number = fields.Char(string="Business License", help="Required for Commercial")


class PropertyFeature(models.Model):
    _name = 'property.feature'
    _description = 'Property Feature'

    name = fields.Char(string='Feature', required=True)
    color = fields.Integer(string='Color Index')
