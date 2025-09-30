from odoo import models, fields, api


class PurchaseDemoLine(models.Model):
    _name = 'purchase.demo.line'
    _description = 'Purchase Demo Line'

    name = fields.Char(string='Description')
    product_id = fields.Many2one('product.product', string='Product')
    quantity = fields.Float(string='Quantity', default=1.0)
    price_unit = fields.Monetary(string='Unit Price')
    price_subtotal = fields.Monetary(string='Subtotal', compute='_compute_subtotal')
    order_id = fields.Many2one('purchase.demo.order', string='Order')
    currency_id = fields.Many2one(related='order_id.currency_id', store=True, readonly=True)

    @api.depends('quantity', 'price_unit')
    def _compute_subtotal(self):
        for line in self:
            line.price_subtotal = line.quantity * (line.price_unit or 0.0)

from odoo import models, fields, api


class PurchaseDemoLine(models.Model):
    _name = 'purchase.demo.line'
    _description = 'Purchase Demo Order Line'

    name = fields.Char(string='Description', required=True)
    product_id = fields.Many2one('product.product', string='Product')
    quantity = fields.Float(string='Quantity', default=1.0)
    price_unit = fields.Monetary(string='Unit Price', default=0.0)
    price_subtotal = fields.Monetary(string='Subtotal', compute='_compute_subtotal')
    order_id = fields.Many2one('purchase.demo.order', string='Order')
    currency_id = fields.Many2one(related='order_id.currency_id', store=True, readonly=True)

    @api.depends('quantity', 'price_unit')
    def _compute_subtotal(self):
        for rec in self:
            rec.price_subtotal = rec.quantity * rec.price_unit
