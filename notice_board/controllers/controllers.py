# -*- coding: utf-8 -*-
# from odoo import http


# class NoticeBoard(http.Controller):
#     @http.route('/notice_board/notice_board', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/notice_board/notice_board/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('notice_board.listing', {
#             'root': '/notice_board/notice_board',
#             'objects': http.request.env['notice_board.notice_board'].search([]),
#         })

#     @http.route('/notice_board/notice_board/objects/<model("notice_board.notice_board"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('notice_board.object', {
#             'object': obj
#         })

