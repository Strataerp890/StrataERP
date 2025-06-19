# -*- coding: utf-8 -*-

from odoo import models, fields, api


class RestrictNegativeStock(models.Model):
    _inherit = 'stock.picking'

	def button_validate(self):
        if self.picking_type_id.code == 'outgoing':
            for move in self.move_ids_without_package:
                product = move.product_id
                demand_qty = move.product_uom_qty
                valuation_layers = self.env['stock.valuation.layer'].search([
                    ('product_id', '=', product.id),
                    ('company_id', '=', self.company_id.id),
                    ('remaining_qty', '>', 0)
                ])
                remaining_qty = sum(valuation_layers.mapped('remaining_qty'))

                if demand_qty > remaining_qty:
                    raise ValidationError(
                        f"Product '{product.display_name}' does not have enough valuation stock.\n"
                        f"Demanded: {demand_qty}, Available (Valuation Layer): {remaining_qty}"
                    )        

        res = super(StockPicking, self).button_validate()

        return res

   

