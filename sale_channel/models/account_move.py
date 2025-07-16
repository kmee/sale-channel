from odoo import fields, models

class AccountMove(models.Model):
    _inherit = "account.move"
    sale_channel_id = fields.Many2one(
        "sale.channel", string="Sale Channel", ondelete="restrict"
    )
