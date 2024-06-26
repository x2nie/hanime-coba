from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):

    _inherit = 'res.config.settings'

    #----------------------------------------------------------
    # Fields
    #----------------------------------------------------------
    
    waterlily_background = fields.Selection(
        related='company_id.waterlily_background',
        readonly=False
    )
