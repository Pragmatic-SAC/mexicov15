# -*- coding: utf-8 -*-
from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    l10n_mx_edi_hazardous_material_code = fields.Char(string="Hazardous Material Designation Code (MX)")
