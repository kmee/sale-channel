print("[DEBUG] sale_channel.models.sale_order.py LOADED")
from odoo import fields, models

class SaleOrder(models.Model):
    _inherit = "sale.order"
    sale_channel_id = fields.Many2one("sale.channel", ondelete="restrict")
    def _prepare_invoice(self):
        res = super()._prepare_invoice()
        res["sale_channel_id"] = self.sale_channel_id.id
        return res
