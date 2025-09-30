from odoo import models, fields, api


class PurchaseDemoOrder(models.Model):
    _name = 'purchase.demo.order'
    _description = 'Purchase Demo Order'

    name = fields.Char(string='Order Reference', required=True, copy=False, default='New')
    partner_id = fields.Many2one('res.partner', string='Vendor', required=True)
    date_order = fields.Datetime(string='Order Date', default=fields.Datetime.now)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('to_approve', 'To Approve'),
        ('approved', 'Approved'),
        ('done', 'Done'),
        ('cancel', 'Cancelled'),
    ], string='Status', default='draft')
    line_ids = fields.One2many('purchase.demo.line', 'order_id', string='Order Lines')
    total_amount = fields.Monetary(string='Total', compute='_compute_total')
    currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.company.currency_id)
    notes = fields.Text(string='Notes')

    approval_level = fields.Integer(string='Approval Level', default=1)

    def action_request_approval(self):
        self.state = 'to_approve'

    def action_approve(self):
        self.state = 'approved'

    def action_done(self):
        self.state = 'done'

    def action_cancel(self):
        self.state = 'cancel'

    @api.depends('line_ids.price_subtotal')
    def _compute_total(self):
        for rec in self:
            rec.total_amount = sum(line.price_subtotal for line in rec.line_ids)
