# -*- coding: utf-8 -*-
{
    'name': "Odoo POS Mock Payment Terminal",
    'summary': "Odoo POS Mock Payment Terminal",
    'description': """
        A mock payment terminal server built to simulate real hardware terminal 
        integration with Odoo 18 Point of Sale (POS).
    """,
    'author': "My Company",
    'website': "https://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/terminal_device_views.xml',
    ],
    'installable': True,
    'application': True,
}

