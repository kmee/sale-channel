from odoo import fields, models

class SaleChannel(models.Model):
    _name = "sale.channel"
    _description = "Sale Channel"
    name = fields.Char(required=True)
    active = fields.Boolean(default=True)
    company_id = fields.Many2one("res.company", default=lambda self: self.env.company)
    channel_type = fields.Selection(
        [],
        help="Allows to use specific fields and actions for a specific channel's type",
    )
