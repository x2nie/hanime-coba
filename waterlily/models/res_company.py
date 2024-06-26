from odoo import models, fields


class ResCompany(models.Model):
    
    _inherit = 'res.company'
    
    waterlily_background = fields.Selection([
        ("image_1", "image 1"), 
        ("image_2", "image 2"),
        ("image_3", "image 3"),
        ("image_4", "image 4"),
    ],"background", default = "image_1", required = True)

    # background_image = fields.Binary(
    #     string='Apps Menu Background Image',
    #     attachment=True
    # )
