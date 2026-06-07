# -*- coding: utf-8 -*-
# from odoo import http


# class PosTerminalDevice(http.Controller):
#     @http.route('/pos_terminal_device/pos_terminal_device', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pos_terminal_device/pos_terminal_device/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('pos_terminal_device.listing', {
#             'root': '/pos_terminal_device/pos_terminal_device',
#             'objects': http.request.env['pos_terminal_device.pos_terminal_device'].search([]),
#         })

#     @http.route('/pos_terminal_device/pos_terminal_device/objects/<model("pos_terminal_device.pos_terminal_device"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pos_terminal_device.object', {
#             'object': obj
#         })

