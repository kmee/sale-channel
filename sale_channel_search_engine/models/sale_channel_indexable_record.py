# Copyright 2022 Akretion (https://www.akretion.com).
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models


class SaleChannelIndexableRecord(models.AbstractModel):
    _name = "sale.channel.indexable.record"
    _inherit = "se.indexable.record"
    _description = "Sale Channel Indexable Record"

    def _synchronize_channel_index(self):
        existing_bindings = self._get_bindings()
        bindings = self.env["se.binding"]
        if "active" in self._fields:
            records = self.filtered("active")
        else:
            records = self
        for channel in records.channel_ids:
            index = channel.search_engine_id.index_ids.filtered(
                lambda s: s.model_id.model == self._name
            )
            if index:
                bindings |= records._add_to_index(index)
        (existing_bindings - bindings).write({"state": "to_delete"})
