from odoo import models
from odoo.tools import format_date

class LeaseSummaryXLSX(models.AbstractModel):
    _name = 'report.property_management.lease_summary_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, leases):
        sheet = workbook.add_worksheet('Lease Summary')
        bold = workbook.add_format({'bold': True})
        currency = workbook.add_format({'num_format': '$#,##0.00'})

        # Headers
        headers = ['Tenant Name', 'Property Name', 'Start Date', 'End Date', 'Monthly Rent', 'Total Rent', 'Status']
        for col, header in enumerate(headers):
            sheet.write(0, col, header, bold)

        # Data
        for row, lease in enumerate(leases, start=1):
            total_rent = lease.monthly_rent * ((lease.end_date - lease.start_date).days / 30)
            sheet.write(row, 0, lease.tenant_id.name)
            sheet.write(row, 1, lease.property_id.name)
            sheet.write(row, 2, format_date(self.env, lease.start_date))
            sheet.write(row, 3, format_date(self.env, lease.end_date))
            sheet.write(row, 4, lease.monthly_rent, currency)
            sheet.write(row, 5, total_rent, currency)
            sheet.write(row, 6, lease.state)