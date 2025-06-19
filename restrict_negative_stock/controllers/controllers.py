# -*- coding: utf-8 -*-
# from odoo import http


# class RestrictNegativeStock(http.Controller):
#     @http.route('/restrict_negative_stock/restrict_negative_stock', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/restrict_negative_stock/restrict_negative_stock/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('restrict_negative_stock.listing', {
#             'root': '/restrict_negative_stock/restrict_negative_stock',
#             'objects': http.request.env['restrict_negative_stock.restrict_negative_stock'].search([]),
#         })

#     @http.route('/restrict_negative_stock/restrict_negative_stock/objects/<model("restrict_negative_stock.restrict_negative_stock"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('restrict_negative_stock.object', {
#             'object': obj
#         })

