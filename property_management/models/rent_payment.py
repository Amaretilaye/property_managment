from odoo import models, fields, api


class RentPayment(models.Model):
    _name = 'rent.payment'
    _description = 'Rent Payment'

    name = fields.Char(string='Payment Reference', required=True, copy=False, readonly=True, default='New')
    lease_id = fields.Many2one('lease.management', string='Lease', required=True)
    payment_date = fields.Date(string='Payment Date', required=True, default=fields.Date.today)
    amount_paid = fields.Float(string='Amount Paid', required=True)
    status = fields.Selection([
        ('paid', 'Paid'),
        ('unpaid', 'Unpaid')
    ], string='Status', default='unpaid')
    note = fields.Text(string='Note')





