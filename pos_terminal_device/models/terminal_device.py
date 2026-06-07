from odoo import fields, models
from requests_toolbelt.downloadutils import stream


class TerminalDevice(models.Model):
    _name = 'terminal.device'
    _description = 'Setting the terminal device'

    name = fields.Char(string='Name of device', required=True)
    ip_address = fields.Char(string='IP address', required=True)
    port = fields.Integer(string='Port', default=9000)
    api_key = fields.Char(string='API Key', required=True)
    active = fields.Boolean(default=True)
    status = fields.Selection([
        ('offline', 'Offline'),
        ('online', 'Online'),
    ], default='offline')