# -*- coding: utf-8 -*-
# from odoo import http


# class ByscoStock(http.Controller):
#     @http.route('/bysco_stock/bysco_stock/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bysco_stock/bysco_stock/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bysco_stock.listing', {
#             'root': '/bysco_stock/bysco_stock',
#             'objects': http.request.env['bysco_stock.bysco_stock'].search([]),
#         })

#     @http.route('/bysco_stock/bysco_stock/objects/<model("bysco_stock.bysco_stock"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bysco_stock.object', {
#             'object': obj
#         })
