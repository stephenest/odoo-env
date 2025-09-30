from odoo import http
from odoo.http import request
import csv
import io


class PurchaseDemoController(http.Controller):
    @http.route('/purchase_demo/export/orders', type='http', auth='user')
    def export_orders(self, **kw):
        orders = request.env['purchase.demo.order'].search([])
        buf = io.StringIO()
        writer = csv.writer(buf)
        writer.writerow(['Order', 'Vendor', 'Date', 'Status', 'Total'])
        for o in orders:
            writer.writerow([o.name, o.partner_id.name or '', o.date_order, o.state, o.total_amount])
        data = buf.getvalue()
        return request.make_response(data, headers=[('Content-Type', 'text/csv'), ('Content-Disposition', 'attachment; filename=purchase_orders.csv')])
