from odoo import models, fields, api


class PurchaseApproval(models.Model):
    _name = 'purchase.demo.approval'
    _description = 'Purchase Demo Approval'

    name = fields.Char(string='Approval Reference', required=True, default='New')
    order_id = fields.Many2one('purchase.demo.order', string='Purchase Order')
    approver_id = fields.Many2one('res.users', string='Approver')
    level = fields.Integer(string='Level', default=1)
    approved = fields.Boolean(string='Approved')
    date = fields.Datetime(string='Date', default=fields.Datetime.now)

    def action_approve(self):
        self.approved = True
        if self.order_id:
            # simple flow: if level >= order approval_level then mark approved
            if self.level >= self.order_id.approval_level:
                self.order_id.state = 'approved'
